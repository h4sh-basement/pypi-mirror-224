
"""
Notify User Upon Completion
"""

from crocodile.comms.notification import Email
import crocodile.toolbox as tb
from crocodile.cluster.remote_machine import ResourceManager
from crocodile.cluster.loader_runner import EmailParams

error_message = ''
exec_times = tb.S()
res_folder = tb.P()

params = EmailParams.from_empty()
manager = ResourceManager.from_pickle(params.resource_manager_path)

print(f'SENDING notification email using `{params.email_config_name}` email configuration ...')

sep = "\n" * 2  # SyntaxError: f-string expression part cannot include a backslash, keep it here outside fstring.
msg = f'''

Hi `{params.addressee}`, I'm `{params.speaker}`, this is a notification that I have completed running the script you sent to me.

``` {params.executed_obj} ```


#### Error Message:
`{error_message}`
#### Execution Times
{exec_times.print(as_config=True, return_str=True)}
#### Executed Shell Script: 
`{manager.shell_script_path}`
#### Executed Python Script: 
`{manager.py_script_path}`

#### Pull results using this script:
`ftprx {params.ssh_conn_str} {res_folder.collapseuser().as_posix()} -r`
Or, using croshell,

```python

ssh = SSH(r'{params.ssh_conn_str}')
ssh.copy_to_here(r'{res_folder.collapseuser().as_posix()}', r=False, zip_first=False)

```

#### Results folder contents:
```

{res_folder.search().print(return_str=True, sep=sep)}

```

'''

try:
    Email.send_and_close(config_name=params.email_config_name, to=params.to_email,
                         subject=f"Execution Completion Notification, job_id = {manager.job_id}", msg=msg)
    print(f'FINISHED sending notification email to `{params.to_email}`')
except Exception as e: print(f"Error sending email: {e}")
