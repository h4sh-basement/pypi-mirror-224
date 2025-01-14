
"""
dl
"""

import crocodile.toolbox as tb
from crocodile.matplotlib_management import ImShow, FigureSave
# from matplotlib.pyplot import hist
import numpy as np
import pandas as pd
from abc import ABC
from typing import Generic, TypeVar, Type, Any, Optional, Union
import enum
from tqdm import tqdm
import copy
from dataclasses import dataclass  # , field


@dataclass
class Specs:
    ip_shapes: list[tuple[int, ...]]
    op_shapes: list[tuple[int, ...]]
    other_shapes: list[tuple[int, ...]]
    ip_names: list[str]  # e.g.: ["x1", "x2"]
    op_names: list[str]  # e.g.: ["y1", "y2"]
    other_names: list[str]  # e.g.: indices or names
    def get_all_strings(self): return self.ip_names + self.op_names + self.other_names


@dataclass
class EvaluationData:
    x: Any
    y_pred: Any
    y_pred_pp: Any
    y_true: Any
    y_true_pp: Any
    names: list[str]
    loss_df: Any


# %% ========================== DeepLearning Accessories =================================


@dataclass
class DeductionResult:
    input: np.ndarray
    preprocessed: np.ndarray
    postprocessed: np.ndarray
    prediction: np.ndarray


class Device(enum.Enum):
    gpu0 = 'gpu0'
    gpu1 = 'gpu1'
    cpu = 'cpu'
    two_gpus = '2gpus'
    auto = 'auto'


@dataclass
class HParams:
    # ===================== Data ==============================
    seed: int
    shuffle: bool
    precision: str
    # ===================== Model =============================
    # depth = 3
    # ===================== Training ==========================
    test_split: float  # test split
    learning_rate: float
    batch_size: int
    epochs: int
    # ================== General ==============================
    name: str  # field(default_factory=lambda: "model-" + tb.randstr(noun=True))
    root: tb.P  # = tb.P.tmp(folder="tmp_models")
    # _configured: bool = False
    # device_na: None = None
    pkg_name: str = 'tensorflow'
    device_name: Device = Device.gpu0
    subpath: str = 'metadata/hyperparameters'  # location within model directory where this will be saved.

    def save(self):
        self.save_dir.joinpath(self.subpath, 'hparams.txt').create(parents_only=True).write_text(str(self))
        try: data = self.__getstate__()
        except AttributeError: data: dict[str, Any] = self.__dict__
        tb.Save.vanilla_pickle(path=self.save_dir.joinpath(self.subpath, "hparams.HParams.dat.pkl"), obj=data)
        tb.Save.vanilla_pickle(path=self.save_dir.joinpath(self.subpath, "hparams.HParams.pkl"), obj=self)
    def __getstate__(self) -> dict[str, Any]: return self.__dict__
    def __setstate__(self, state: dict): return self.__dict__.update(state)
    @classmethod
    def from_saved_data(cls, path, *args, **kwargs) -> 'HParams':
        data: dict = tb.Read.vanilla_pickle(path=tb.P(path) / cls.subpath / "hparams.HParams.dat.pkl", *args, **kwargs)
        return cls(**data)
    def __repr__(self, **kwargs): return "HParams Object with specs:\n" + tb.Struct(self.__dict__).print(as_config=True, return_str=True)
    @property
    def pkg(self):
        if self.pkg_name not in ("tensorflow", "torch"): raise ValueError(f"pkg_name must be either `tensorflow` or `torch`")
        return __import__("tensorflow") if self.pkg_name == "tensorflow" else __import__("torch")
    @property
    def save_dir(self) -> tb.P: return (tb.P(self.root) / self.name).create()


SubclassedHParams = TypeVar("SubclassedHParams", bound=HParams)
def _silence_pylance(hp: SubclassedHParams) -> SubclassedHParams: return hp


class DataReader:
    subpath = tb.P("metadata/data_reader")
    """This class holds the dataset for training and testing. However, it also holds meta data for preprocessing
    and postprocessing. The latter is essential at inference time_produced, but the former need not to be saved. As such,
    at save time_produced, this class only remember the attributes inside `.specs` `Struct`. Thus, whenever encountering
    such type of data, make sure to keep them inside that `Struct`. Lastly, for convenience purpose, the class has
    implemented a fallback `getattr` method that allows accessing those attributes from the class data_only, without the
    need to reference `.dataspects`.
    """
    def get_pandas_profile_path(self, suffix: str) -> tb.P: return self.hp.save_dir.joinpath(self.subpath, f"pandas_profile_report_{suffix}.html").create(parents_only=True)
    def __init__(self, hp: SubclassedHParams, specs: Optional[Specs] = None, split: Optional[dict[str, np.ndarray]] = None) -> None:
        super().__init__()
        self.hp = hp
        self.split = split
        self.plotter = None
        self.specs: Specs = Specs(ip_shapes=[], op_shapes=[], other_shapes=[], ip_names=[], op_names=[], other_names=[]) if specs is None else specs
        # self.df_handler = df_handler
    def save(self, path: Optional[str] = None, **kwargs) -> None:
        _ = kwargs
        base = (tb.P(path) if path is not None else self.hp.save_dir).joinpath(self.subpath).create()
        try: data = self.__getstate__()
        except AttributeError: data: dict[str, Any] = self.__dict__
        tb.Save.vanilla_pickle(path=base / "data_reader.DataReader.dat.pkl", obj=data)
        tb.Save.vanilla_pickle(path=base / "data_reader.DataReader.pkl", obj=self)
    @classmethod
    def from_saved_data(cls, path: Union[str, tb.P], hp: HParams, *args, **kwargs):
        path = tb.P(path) / cls.subpath / "data_reader.DataReader.dat.pkl"
        data: dict = tb.Read.vanilla_pickle(path)
        obj = cls(hp=hp, *args, **kwargs)
        obj.__setstate__(data)
        return obj
    def __getstate__(self) -> dict[str, Any]:
        items = ["specs"]
        res = {}
        for item in items:
            if hasattr(self, item): res[item] = getattr(self, item)
        return res
    def __setstate__(self, state): return self.__dict__.update(state)
    def __repr__(self): return f"DataReader Object with these keys: \n" + tb.Struct(self.__dict__).print(as_config=False, return_str=True)

    def split_the_data(self, *args, **kwargs) -> None:
        from sklearn.model_selection import train_test_split
        result = train_test_split(*args, test_size=self.hp.test_split, shuffle=self.hp.shuffle, random_state=self.hp.seed, **kwargs)
        self.split = dict(train_loader=None, test_loader=None)
        if self.specs.ip_names is None:
            ip_names: list[str] = [f"x_{i}" for i in range(len(args) - 1)]
            if len(ip_names) == 1: ip_names = ["x"]
            self.specs.ip_names = ip_names
        if self.specs.op_names is None: self.specs.op_names = ["y"]
        if self.specs.other_names is None: self.specs.other_names = []
        strings = self.specs.get_all_strings()
        assert len(strings) == len(args), f"Number of strings must match number of args. Got {len(strings)} strings and {len(args)} args."
        for an_arg, key in zip(args, strings):
            a_shape = an_arg.iloc[0].shape if type(an_arg) in {pd.DataFrame, pd.Series} else np.array(an_arg[0]).shape
            if key in self.specs.ip_names: self.specs.ip_shapes.append(a_shape)
            elif key in self.specs.op_names: self.specs.op_shapes.append(a_shape)
            elif key in self.specs.other_names: self.specs.other_shapes.append(a_shape)
        self.split.update({astring + '_train': result[ii * 2] for ii, astring in enumerate(strings)})
        self.split.update({astring + '_test': result[ii * 2 + 1] for ii, astring in enumerate(strings)})
        print(f"================== Training Data Split ===========================")
        tb.Struct(self.split).print()

    def get_data_strings(self, which_data="ip", which_split="train"):
        strings = {"op": self.specs.op_names, "ip": self.specs.ip_names, "others": self.specs.other_names}[which_data]
        keys_ip = [item + f"_{which_split}" for item in strings]
        return keys_ip

    def sample_dataset(self, aslice=None, indices=None, use_slice=False, split="test", size=None):
        assert self.split is not None, f"No dataset is loaded to DataReader, .split attribute is empty. Consider using `.load_training_data()` method."
        keys_ip = self.get_data_strings(which_data="ip", which_split=split)
        keys_op = self.get_data_strings(which_data="op", which_split=split)
        keys_others = self.get_data_strings(which_data="others", which_split=split)
        tmp = self.split[keys_ip[0]]
        assert tmp is not None, f"Split key {keys_ip[0]} is None. Make sure that the data is loaded."
        ds_size = len(tmp)
        select_size = size or self.hp.batch_size
        start_idx = np.random.choice(ds_size - select_size)

        if indices is not None: selection = indices
        elif aslice is not None: selection = aslice
        elif use_slice: selection = slice(start_idx, start_idx + select_size)  # ragged tensors don't support indexing, this can be handy in that case.
        else: selection = np.random.choice(ds_size, size=select_size, replace=False)

        x, y, others = [], [], []
        for idx, key in zip([0] * len(keys_ip) + [1] * len(keys_op) + [2] * len(keys_others), keys_ip + keys_op + keys_others):
            tmp = self.split[key]
            if isinstance(tmp, (pd.DataFrame, pd.Series)): item = tmp.iloc[selection]
            elif tmp is not None: item = tmp[selection]
            else: raise ValueError(f"Split key {key} is None. Make sure that the data is loaded.")
            if idx == 0: x.append(item)
            elif idx == 1: y.append(item)
            else: others.append(item)
        x = x[0] if len(self.specs.ip_names) == 1 else x
        y = y[0] if len(self.specs.op_names) == 1 else y
        others = others[0] if len(self.specs.other_names) == 1 else others
        if len(others) == 0:
            # others = np.arange(len(x if len(self.ip_strings) == 1 else x[0]))
            if type(selection) is slice:
                others = np.arange(*selection.indices(10000000000000))
            else:
                others = selection
        return x, y, others

    def get_random_inputs_outputs(self, ip_shapes=None, op_shapes=None):
        if ip_shapes is None: ip_shapes = self.specs.ip_shapes
        if op_shapes is None: op_shapes = self.specs.op_shapes
        dtype = self.hp.precision if hasattr(self.hp, "precision") else "float32"
        x = [np.random.randn(self.hp.batch_size, * ip_shape).astype(dtype) for ip_shape in ip_shapes]
        y = [np.random.randn(self.hp.batch_size, * op_shape).astype(dtype) for op_shape in op_shapes]
        x = x[0] if len(self.specs.ip_names) == 1 else x
        y = y[0] if len(self.specs.op_names) == 1 else y
        return x, y

    def preprocess(self, *args, **kwargs): _ = args, kwargs, self; return args[0]  # acts like identity.
    def postprocess(self, *args, **kwargs): _ = args, kwargs, self; return args[0]  # acts like identity

    # def standardize(self):
    #     assert self.split is not None, "Load up the data first before you standardize it."
    #     self.scaler = StandardScaler()
    #     self.split['x_train'] = self.scaler.fit_transform(self.split['x_train'])
    #     self.split['x_test']= self.scaler.transform(self.split['x_test'])

    def image_viz(self, pred, gt=None, names=None, **kwargs):
        """
        Assumes numpy inputs
        """
        if gt is None: self.plotter = ImShow(pred, labels=None, sup_titles=names, origin='lower', **kwargs)
        else: self.plotter = ImShow(img_tensor=pred, sup_titles=names, labels=['Reconstruction', 'Ground Truth'], origin='lower', **kwargs)

    def viz(self, *args, **kwargs):
        """Implement here how you would visualize a batch of input and ouput pair. Assume Numpy arguments rather than tensors."""
        _ = self, args, kwargs
        return None


SubclassedDataReader = TypeVar("SubclassedDataReader", bound=DataReader)


@dataclass
class Compiler:
    loss: Any
    optimizer: Any
    metrics: list[Any]


class BaseModel(ABC):
    """My basic model. It implements the following methods:

    * :func:`BaseModel.preprocess` This should convert to tensors as appropriate for the model.
    * :func:`BaseModel.postprocess` This method should convert back to numpy arrays.
    * :func:`BaseModel.infer` This method expects processed input and only forwards through the model
    * :func:`BaseModel.predict` expects a processed input, uese infer and does postprocessing.
    * :func:`BaseModel.predict_from_s` reads, preprocess, then uses predict method.
    * :func:`BseModel.evaluate` Expects processed input and internally calls infer and postprocess methods.

    Functionally or Sequentually built models are much more powerful than Subclassed models. They are faster, have more features, can be plotted, serialized, correspond to computational graphs etc.
    """
    # @abstractmethod
    def __init__(self, hp: SubclassedHParams, data: SubclassedDataReader, compiler: Optional[Compiler] = None, history: Optional[list[dict]] = None):
        # : Optional[list]
        self.hp = hp  # should be populated upon instantiation.
        self.data = data  # should be populated upon instantiation.
        self.model: Any = self.get_model()  # should be populated upon instantiation.
        self.compiler = compiler  # Struct with .losses, .metrics and .optimizer.
        self.history = history if history is not None else []  # should be populated in fit method, or loaded up.
        self.plotter = FigureSave.NullAuto
        self.fig = None
        self.kwargs = None
        self.tmp = None
    def get_model(self):
        raise NotImplementedError
        # pass
    def compile(self, loss: Optional[Any] = None, optimizer: Optional[Any] = None, metrics: Optional[list[Any]] = None, compile_model=True):
        """ Updates compiler attributes. This acts like a setter.
        .. note:: * this method is as good as setting attributes of `compiler` directly in case of PyTorch.
                  * In case of TF, this is not the case as TF requires actual futher different
                    compilation before changes take effect.
        Remember:
        * Must be run prior to fit method.
        * Can be run only after defining model attribute.
        """
        pkg = self.hp.pkg
        if self.hp.pkg_name == 'tensorflow':
            if loss is None: loss = pkg.keras.losses.MeanSquaredError()
            if optimizer is None: optimizer = pkg.keras.optimizers.Adam(self.hp.learning_rate)
            if metrics is None: metrics = []  # [pkg.keras.metrics.MeanSquaredError()]
        elif self.hp.pkg_name == 'torch':
            if loss is None: loss = pkg.nn.MSELoss()
            if optimizer is None: optimizer = pkg.optim.Adam(self.model.parameters(), lr=self.hp.learning_rate)
            if metrics is None: metrics = []  # [tmp.MeanSquareError()]
        else: raise ValueError(f"pkg_name must be either `tensorflow` or `torch`")
        # Create a new compiler object
        self.compiler = Compiler(loss=loss, optimizer=optimizer, metrics=list(metrics))
        # in both cases: pass the specs to the compiler if we have TF framework
        if self.hp.pkg.__name__ == "tensorflow" and compile_model: self.model.compile(**self.compiler.__dict__)

    def fit(self, viz: bool = True, val_sample_weights: Optional[np.ndarray] = None, **kwargs):
        assert self.data.split is not None, "Split your data before you start fitting."
        x_train = [self.data.split[item] for item in self.data.get_data_strings(which_data="ip", which_split="train")]
        y_train = [self.data.split[item] for item in self.data.get_data_strings(which_data="op", which_split="train")]
        x_test = [self.data.split[item] for item in self.data.get_data_strings(which_data="ip", which_split="test")]
        y_test = [self.data.split[item] for item in self.data.get_data_strings(which_data="op", which_split="test")]
        x_test = x_test[0] if len(x_test) == 1 else x_test
        y_test = y_test[0] if len(y_test) == 1 else y_test
        default_settings = dict(x=x_train[0] if len(x_train) == 1 else x_train,
                                y=y_train[0] if len(y_train) == 1 else y_train,
                                validation_data=(x_test, y_test) if val_sample_weights is None else (x_test, y_test, val_sample_weights),
                                batch_size=self.hp.batch_size, epochs=self.hp.epochs, verbose=1, shuffle=self.hp.shuffle, callbacks=[])
        default_settings.update(kwargs)
        hist = self.model.fit(**default_settings)
        self.history.append(copy.deepcopy(hist.history))  # it is paramount to copy, cause source can change.
        if viz:
            artist = self.plot_loss()
            artist.fig.savefig(self.hp.save_dir.joinpath(f"metadata/training/loss_curve.png").append(index=True).create(parents_only=True))
        return self

    def switch_to_sgd(self, epochs: int = 10):
        assert self.compiler is not None, "Compiler is not initialized. Please initialize the compiler first."
        print(f'Switching the optimizer to SGD. Loss is fixed to {self.compiler.loss}'.center(100, '*'))
        if self.hp.pkg.__name__ == 'tensorflow': new_optimizer = self.hp.pkg.keras.optimizers.SGD(lr=self.hp.learning_rate * 0.5)
        else: new_optimizer = self.hp.pkg.optim.SGD(self.model.parameters(), lr=self.hp.learning_rate * 0.5)
        self.compiler.optimizer = new_optimizer
        return self.fit(epochs=epochs)

    def switch_to_l1(self, epochs: int = 10):
        assert self.compiler is not None, "Compiler is not initialized. Please initialize the compiler first."
        if self.hp.pkg.__name__ == 'tensorflow':
            self.model.reset_metrics()
        print(f'Switching the loss to l1. Optimizer is fixed to {self.compiler.optimizer}'.center(100, '*'))
        if self.hp.pkg.__name__ == 'tensorflow':
            new_loss = self.hp.pkg.keras.losses.MeanAbsoluteError()
        else:
            import crocodile.deeplearning_torch as tmp
            new_loss = tmp.MeanAbsoluteError()
        self.compiler.loss = new_loss
        return self.fit(epochs=epochs)

    def preprocess(self, *args, **kwargs):
        """Converts an object to a numerical form consumable by the NN."""
        return self.data.preprocess(*args, **kwargs)

    def postprocess(self, *args, **kwargs): return self.data.postprocess(*args, **kwargs)
    def __call__(self, *args, **kwargs): return self.model(*args, **kwargs)
    def viz(self, *args, **kwargs): return self.data.viz(*args, **kwargs)
    def save_model(self, directory): self.model.save(directory)  # In TF: send only path dir. Save path is saved_model.pb
    def save_weights(self, directory): self.model.save_weights(directory.joinpath(self.model.name))  # TF: last part of path is file path.
    @staticmethod
    def load_model(directory: tb.P): __import__("tensorflow").keras.models.load_model(str(directory))  # path to directory. file saved_model.pb is read auto.
    def load_weights(self, directory):
        # assert self.model is not None, "Model is not initialized. Please initialize the model first."
        self.model.load_weights(directory.glob('*.data*').__next__().__str__().split('.data')[0])  # requires path to file path.
    def summary(self):
        from contextlib import redirect_stdout
        path = self.hp.save_dir.joinpath("metadata/model/model_summary.txt").create(parents_only=True)
        with open(str(path), 'w', encoding='utf-8') as f:
            with redirect_stdout(f): self.model.summary()
        return self.model.summary()
    def config(self): _ = [print(layer.get_config(), "\n==============================") for layer in self.model.layers]; return None
    def plot_loss(self, *args, **kwargs):
        res = tb.Struct.concat_values(*self.history)
        assert self.compiler is not None, "Compiler is not initialized. Please initialize the compiler first."
        if hasattr(self.compiler.loss, "name"): y_label = self.compiler.loss.name
        else: y_label = self.compiler.loss.__name__
        return res.plot(*args, title="Loss Curve", xlabel="epochs", ylabel=y_label, **kwargs)

    def infer(self, x) -> np.ndarray:
        """ This method assumes numpy input, datatype-wise and is also preprocessed.
        NN is put in eval mode.
        :param x:
        :return: prediction as numpy
        """
        return self.model.predict(x)  # Keras automatically handles special layers, can accept dataframes, and always returns numpy.

    def predict(self, x, **kwargs):
        """This method assumes preprocessed input. Returns postprocessed output. It is useful at evaluation time with preprocessed test set."""
        return self.postprocess(self.infer(x), **kwargs)

    def deduce(self, obj, viz=True, **kwargs) -> DeductionResult:
        """Assumes that contents of the object are in the form of a batch."""
        preprocessed = self.preprocess(obj, **kwargs)
        prediction = self.infer(preprocessed)
        postprocessed = self.postprocess(prediction, **kwargs)
        result = DeductionResult(input=obj, preprocessed=preprocessed, prediction=prediction, postprocessed=postprocessed)
        if viz: self.viz(postprocessed, **kwargs)
        return result

    def evaluate(self, x_test=None, y_test=None, names_test=None, aslice=None, indices=None, use_slice=False, size=None, split="test", viz=True, viz_kwargs=None, **kwargs):
        if x_test is None and y_test is None and names_test is None:
            x_test, y_test, names_test = self.data.sample_dataset(aslice=aslice, indices=indices, use_slice=use_slice, split=split, size=size)
        elif names_test is None and x_test is not None: names_test = np.arange(len(x_test))
        else: raise ValueError(f"Either provide x_test and y_test or none of them. Got x_test={x_test} and y_test={y_test}")
        # ==========================================================================
        y_pred = self.infer(x_test)
        loss_df = self.get_metrics_evaluations(y_pred, y_test)
        if loss_df is not None:
            if len(self.data.specs.other_names) == 1: loss_df[self.data.specs.other_names[0]] = names_test
            else:
                for val, name in zip(names_test, self.data.specs.other_names): loss_df[name] = val
        y_pred_pp = self.postprocess(y_pred, per_instance_kwargs=dict(name=names_test), legend="Prediction", **kwargs)
        y_true_pp = self.postprocess(y_test, per_instance_kwargs=dict(name=names_test), legend="Ground Truth", **kwargs)
        results = EvaluationData(x=x_test, y_pred=y_pred, y_pred_pp=y_pred_pp, y_true=y_test, y_true_pp=y_true_pp, names=[str(item) for item in names_test], loss_df=loss_df)
        if viz:
            loss_name = results.loss_df.columns.to_list()[0]  # first loss path
            loss_label = results.loss_df[loss_name].apply(lambda x: f"{loss_name} = {x}").to_list()
            names = [f"{aname}. Case: {anindex}" for aname, anindex in zip(loss_label, names_test)]
            self.fig = self.viz(y_pred_pp, y_true_pp, names=names, **(viz_kwargs or {}))
        return results

    def get_metrics_evaluations(self, prediction, groun_truth) -> Optional[pd.DataFrame]:
        if self.compiler is None: return None
        metrics = tb.L([self.compiler.loss]) + self.compiler.metrics
        loss_dict: dict[str, list] = dict()
        for a_metric in metrics:
            if hasattr(a_metric, "name"): name = a_metric.name
            elif hasattr(a_metric, "__name__"): name = a_metric.__name__
            else: name = "unknown_loss_name"
            # try:  # EAFP vs LBYL: both are duck-typing styles as they ask for what object can do (whether by introspection or trial) as opposed to checking its type.
            #     path = a_metric.path  # works for subclasses Metrics
            # except AttributeError: path = a_metric.__name__  # works for functions.
            loss_dict[name] = []
            for a_prediction, a_y_test in zip(prediction, groun_truth):
                if hasattr(a_metric, "reset_states"): a_metric.reset_states()
                loss = a_metric(y_pred=a_prediction[None], y_true=a_y_test[None])
                loss_dict[name].append(np.array(loss).item())
        return pd.DataFrame(loss_dict)

    def save_class(self, weights_only: bool = True, version: str = '0', **kwargs):
        """Simply saves everything:
        1. Hparams
        2. Data specs
        3. Model architecture or weights depending on the following argument.
        :param version: Model version, up to the user.
        :param weights_only: self-explanatory
        :return:
        """
        self.hp.save()  # goes into the meta path.
        self.data.save()  # goes into the meta path.
        tb.Save.vanilla_pickle(obj=self.history, path=self.hp.save_dir / 'metadata/training/history.pkl', verbose=True, desc="Training History")  # goes into the meta path.
        try: tb.Experimental.generate_readme(self.hp.save_dir, obj=self.__class__, **kwargs)
        except Exception as ex: print(ex)  # often fails because model is defined in main during experiments.
        save_dir = self.hp.save_dir.joinpath(f'{"weights" if weights_only else "model"}_save_v{version}').create()  # model save goes into data path.
        if weights_only: self.save_weights(save_dir)
        else: self.save_model(save_dir)
        import importlib
        __module = self.__class__.__module__
        if __module.startswith('__main__'):
            raise RuntimeError("Model class is defined in main. Saving the code from the current working directory. Consider importing the model class from a module.")
        try:
            module = importlib.import_module(__module)
        except ModuleNotFoundError as ex:
            print(ex)
            module = None
        if module is not None and hasattr(module, '__file__') and module.__file__ is not None:
            module_path_rh = tb.P(module.__file__).resolve().collapseuser().as_posix()
        else:
            module_path_rh = None
        specs = {'__module__': __module,
                 'model_class': self.__class__.__name__,
                 'data_class': self.data.__class__.__name__,
                 'hp_class': self.hp.__class__.__name__,
                 # the above is sufficient if module comes from installed package. Otherwise, if its from a repo, we need to add the following:
                 'module_path_rh': module_path_rh,
                 'cwd_rh': tb.P.cwd().collapseuser().as_posix(),
                 }
        tb.Save.json(obj=specs, path=self.hp.save_dir.joinpath('metadata/code_specs.json').str)
        print(f'SAVED Model Class @ {self.hp.save_dir.as_uri()}')
        return self.hp.save_dir

    @classmethod
    def from_class_weights(cls, path, hparam_class: Optional[SubclassedHParams] = None, data_class: Optional[SubclassedDataReader] = None, device_name: Optional[Device] = None, verbose: bool = True):
        path = tb.P(path)
        if hparam_class is not None: hp_obj = hparam_class.from_saved_data(path)
        else: hp_obj = tb.Read.vanilla_pickle(path=(path / HParams.subpath + "hparams.HyperParam.pkl"))
        if device_name: hp_obj.device_name = device_name
        if data_class is not None: d_obj = data_class.from_saved_data(path, hp=hp_obj)
        else: d_obj = tb.Read.vanilla_pickle(path=path / DataReader.subpath / "data_reader.DataReader.pkl")
        if hp_obj.root != path.parent: hp_obj.root, hp_obj.name = path.parent, path.name  # if user moved the file to somewhere else, this will help alighment with new directory in case a modified version is to be saved.
        # if type(hp_obj) is Generic[HParams]:
        d_obj.hp = hp_obj
        # else:rd
            # raise ValueError(f"hp_obj must be of type `HParams` or `Generic[HParams]`. Got {type(hp_obj)}")
        model_obj: 'BaseModel' = cls(hp_obj, d_obj)
        model_obj.load_weights(list(path.search('*_save_*'))[0])
        history_path = path / "metadata/training/history.pkl"
        if history_path.exists(): history: list = tb.Read.vanilla_pickle(path=history_path)
        else: history = []
        model_obj.history = history
        _ = print(f"LOADED {model_obj.__class__}: {model_obj.hp.name}") if verbose else None
        return model_obj

    @classmethod
    def from_class_model(cls, path):
        path = tb.P(path)
        hp_obj = HParams.from_saved_data(path)
        data_obj = DataReader.from_saved_data(path, hp=hp_obj)
        directory = path.search('*_save_*')
        model_obj = cls.load_model(list(directory)[0])
        wrapper_class = cls(hp_obj, data_obj, model_obj)
        return wrapper_class

    @staticmethod
    def from_path(path_model, **kwargs):
        path_model = tb.P(path_model).expanduser().absolute()
        specs = tb.Read.json(path=path_model.joinpath('metadata/code_specs.json'))
        print(f"Loading up module: `{specs['__module__']}`.")
        import importlib
        try:
            module = importlib.import_module(specs['__module__'])
        except ModuleNotFoundError as ex:
            print(ex)
            print(f"ModuleNotFoundError: Attempting to try again after appending path with `cwd`: `{specs['cwd_rh']}`.")
            import sys
            sys.path.append(tb.P(specs['cwd_rh']).expanduser().absolute().str)
            try:
                module = importlib.import_module(specs['__module__'])
            except ModuleNotFoundError as ex2:
                print(ex2)
                print(f"ModuleNotFoundError: Attempting to directly loading up `module_path`: `{specs['module_path_rh']}`.")
                module = load_class(tb.P(specs['module_path_rh']).expanduser().absolute().as_posix())
        model_class: BaseModel = getattr(module, specs['model_class'])
        data_class: DataReader = getattr(module, specs['data_class'])
        hp_class: HParams = getattr(module, specs['hp_class'])
        return model_class.from_class_weights(path_model, hparam_class=hp_class, data_class=data_class, **kwargs)

    def plot_model(self, dpi=150, **kwargs):  # alternative viz via tf2onnx then Netron.
        import tensorflow as tf
        path = self.hp.save_dir.joinpath("metadata/model/model_plot.png")
        tf.keras.utils.plot_model(self.model, to_file=str(path), show_shapes=True, show_layer_names=True, show_layer_activations=True, show_dtype=True, expand_nested=True, dpi=dpi, **kwargs)
        print(f"Successfully plotted the model @ {path.as_uri()}")
        return path

    def build(self, sample_dataset=False, ip_shapes=None, ip=None, verbose=True):
        """ Building has two main uses.
        * Useful to baptize the model, especially when its layers are built lazily. Although this will eventually happen as the first batch goes in. This is a must before showing the summary of the model.
        * Doing sanity check about shapes when designing model.
        * Sanity check about values and ranges when random normal input is fed.
        :param sample_dataset:
        :param ip_shapes:
        :param ip:
        :param verbose:
        :return:
        """
        try:
            keys_ip = self.data.get_data_strings(which_data="ip", which_split="test")
            keys_op = self.data.get_data_strings(which_data="op", which_split="test")
        except TypeError as te:
            raise ValueError(f"Failed to load up sample data. Make sure that data has been loaded up properly.") from te

        if ip is None:
            if sample_dataset: ip, _, _ = self.data.sample_dataset()
            else: ip, _ = self.data.get_random_inputs_outputs(ip_shapes=ip_shapes)
        op = self.model(inputs=ip)
        ops = [op] if len(keys_op) == 1 else op
        ips = [ip] if len(keys_ip) == 1 else ip
        if verbose:
            print("\n")
            print("Build Test".center(50, '-'))
            tb.Struct.from_keys_values(keys_ip, tb.L(ips).apply(lambda x: x.shape)).print(as_config=True, title="Input shapes:")
            tb.Struct.from_keys_values(keys_op, tb.L(ops).apply(lambda x: x.shape)).print(as_config=True, title=f"Output shape:")
            print("\n\nStats on output data for random normal input:")
            try:
                res = []
                for item_str, item_val in zip(keys_ip + keys_op, list(ips) + list(ops)):
                    a_df = pd.DataFrame(np.array(item_val).flatten()).describe().rename(columns={0: item_str})
                    res.append(a_df)
                print(pd.concat(res, axis=1))
            except Exception as ex:
                print(f"Could not do stats on outputs and inputs. Error: {ex}")
            print("Build Test Finished".center(50, '-'))
            print("\n")


SubclassedBaseModel = TypeVar("SubclassedBaseModel", bound=BaseModel)


class Ensemble(tb.Base):
    def __init__(self, hp_class: Type[SubclassedHParams], data_class: Type[SubclassedDataReader], model_class: Type[SubclassedBaseModel], size=10, **kwargs):
        """
        :param model_class: Either a class for constructing saved_models or list of saved_models already cosntructed.
          * In either case, the following methods should be implemented:
          __init__, load, load_weights, save, save_weights, predict, fit
          Model constructor should takes everything it needs from self.hp and self.data only.
          Otherwise, you must pass a list of already constructed saved_models.
        :param size: size of ensemble
        """
        super().__init__(**kwargs)
        self.__dict__.update(kwargs)
        self.size = size
        self.hp_class = hp_class
        self.data_class = data_class
        self.model_class = model_class
        self.models: list[BaseModel] = []
        # self.data = None  # one data object for all models (so that it can fit in the memory)
        if hp_class and data_class and model_class:
            # only generate the dataset once and attach it to the ensemble to be reused by models.
            self.data = self.data_class(hp=hp_class())
            print("Creating Models".center(100, "="))
            for i in tqdm(range(size)):
                hp = self.hp_class()
                hp.name = str(hp.name) + f'__model__{i}'
                datacopy: SubclassedDataReader = copy.copy(self.data)  # shallow copy
                datacopy.hp = hp  # type: ignore
                self.models.append(model_class(hp, datacopy))
        self.performance = None

    @classmethod
    def from_saved_models(cls, parent_dir, model_class: Type[SubclassedBaseModel], hp_class: Type[SubclassedHParams], data_class: Type[SubclassedDataReader]) -> 'Ensemble':
        obj = cls(hp_class=hp_class, data_class=data_class, model_class=model_class, path=parent_dir, size=len(tb.P(parent_dir).search('*__model__*')))
        obj.models = list(tb.P(parent_dir).search(pattern='*__model__*').apply(model_class.from_class_model))
        return obj

    @classmethod
    def from_saved_weights(cls, parent_dir, model_class: Type[SubclassedBaseModel], hp_class: Type[SubclassedHParams], data_class: Type[SubclassedDataReader]) -> 'Ensemble':
        obj = cls(model_class=model_class, hp_class=hp_class, data_class=data_class, path=parent_dir, size=len(tb.P(parent_dir).search('*__model__*')))
        obj.models = list(tb.P(parent_dir).search('*__model__*').apply(model_class.from_class_weights))
        return obj

    @staticmethod
    def from_path(path) -> list[SubclassedBaseModel]: return list(tb.P(path).expanduser().absolute().search("*").apply(BaseModel.from_path))

    def fit(self, shuffle_train_test=True, save=True, **kwargs):
        self.performance = []
        for i in range(self.size):
            print('\n\n', f" Training Model {i} ".center(100, "*"), '\n\n')
            if shuffle_train_test:
                self.models[i].hp.seed = np.random.randint(0, 1000)
                self.data.split_the_data()  # shuffle data (shared among models)
            self.models[i].fit(**kwargs)
            self.performance.append(self.models[i].evaluate(idx=slice(0, -1), viz=False))
            if save:
                self.models[i].save_class()
                tb.Save.vanilla_pickle(obj=self.performance, path=self.models[i].hp.save_dir / "performance.pkl")
        print("\n\n", f" Finished fitting the ensemble ".center(100, ">"), "\n")

    def clear_memory(self): pass  # t.cuda.empty_cache()


class Losses:
    @staticmethod
    def get_log_square_loss_class():
        import tensorflow as tf

        class LogSquareLoss(tf.keras.losses.Loss):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.name = "LogSquareLoss"

            def call(self, y_true, y_pred):
                _ = self
                tmp = tf.math.log(tf.convert_to_tensor(10.0, dtype=y_pred.dtype))
                factor = tf.Tensor(20) / tmp
                return factor * tf.math.log(tf.reduce_mean((y_true - y_pred)**2))
        return LogSquareLoss

    @staticmethod
    def get_mean_max_error(tf):
        """
        For Tensorflow
        """
        class MeanMaxError(tf.keras.metrics.Metric):
            def __init__(self, name='MeanMaximumError', **kwargs):
                super(MeanMaxError, self).__init__(name=name, **kwargs)
                self.mme = self.add_weight(name='mme', initializer='zeros')
                self.__name__ = name

            def update_state(self, y_true, y_pred, sample_weight=None): self.mme.assign(tf.reduce_mean(tf.reduce_max(sample_weight or 1.0 * tf.abs(y_pred - y_true), axis=1)))
            def result(self): return self.mme
            def reset_states(self): self.mme.assign(0.0)
        return MeanMaxError


class HPTuning:
    def __init__(self):
        # ================== Tuning ===============
        from tensorboard.plugins.hparams import api as hpt
        self.hpt = hpt
        import tensorflow as tf
        self.pkg = tf
        self.dir = None
        self.params = tb.List()
        self.acc_metric = None
        self.metrics = None

    @staticmethod
    def help():
        """Steps of use: subclass this and do the following:
        * Set directory attribute.
        * set params
        * set accuracy metric
        * generate writer.
        * implement run method.
        * run loop method.
        * in the command line, run `tensorboard --logdir <self.dir>`
        """
        pass

    def run(self, param_dict):
        _, _ = self, param_dict
        # should return a result that you want to maximize
        return _

    # def gen_writer(self):
    #     import tensorflow as tf
    #     with tf.summary.create_file_writer(str(self.dir)).as_default():
    #         self.hpt.hparams_config(
    #             hparams=self.params,
    #             metrics=self.metrics)

    # def loop(self):
    #     import itertools
    #     counter = -1
    #     tmp = self.params.list[0].domain.values
    #     for combination in itertools.product(*[tmp]):
    #         counter += 1
    #         param_dict = dict(zip(self.params.list, combination))
    #         with self.pkg.summary.create_file_writer(str(self.dir / f"run_{counter}")).as_default():
    #             self.hpt.hparams(param_dict)  # record the values used in this trial
    #             accuracy = self.run(param_dict)
    #             self.pkg.summary.scalar(self.acc_metric, accuracy, step=1)

    # def optimize(self): self.gen_writer(); self.loop()


class KerasOptimizer:
    def __init__(self, d):
        self.data = d
        self.tuner = None

    def __call__(self, ktp): pass

    def tune(self):
        kt = tb.core.install_n_import("kerastuner")
        self.tuner = kt.Hyperband(self, objective='loss', max_epochs=10, factor=3, directory=tb.P.tmp('my_dir'), project_name='intro_to_kt')


def batcher(func_type='function'):
    if func_type == 'method':
        def batch(func):
            # from functools import wraps
            # @wraps(func)
            def wrapper(self, x, *args, per_instance_kwargs=None, **kwargs):
                output = []
                for counter, item in enumerate(x):
                    mykwargs = {key: value[counter] for key, value in per_instance_kwargs.items()} if per_instance_kwargs is not None else {}
                    output.append(func(self, item, *args, **mykwargs, **kwargs))
                return np.array(output)
            return wrapper
        return batch
    elif func_type == 'class': raise NotImplementedError
    elif func_type == 'function':
        class Batch(object):
            def __init__(self, func): self.func = func
            def __call__(self, x, **kwargs): return np.array([self.func(item, **kwargs) for item in x])
        return Batch


def batcherv2(func_type='function', order=1):
    if func_type == 'method':
        def batch(func):
            # from functools import wraps
            # @wraps(func)
            def wrapper(self, *args, **kwargs): return np.array([func(self, *items, *args[order:], **kwargs) for items in zip(*args[:order])])
            return wrapper
        return batch
    elif func_type == 'class': raise NotImplementedError
    elif func_type == 'function':
        class Batch(object):
            def __init__(self, func): self.func = func
            def __call__(self, *args, **kwargs): return np.array([self.func(self, *items, *args[order:], **kwargs) for items in zip(*args[:order])])
        return Batch


def get_template():
    tb.install_n_import("clipboard").copy(tb.P(__file__).parent.joinpath("msc/dl_template.py").read_text(encoding="utf-8"))
    print("Copied to clipboard")


def load_class(file_path: str):
    import importlib.util
    module_spec = importlib.util.spec_from_file_location(name="__temp_module__", location=file_path)
    if module_spec is None: raise ValueError(f"Failed to load up module from path: {file_path}")
    module = importlib.util.module_from_spec(module_spec)
    assert module_spec.loader is not None, "Module loader is None."
    module_spec.loader.exec_module(module)
    return module


if __name__ == '__main__':
    pass
