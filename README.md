# A simple  boilerplate template for Python in VS Code!

1. Open the Command Palette (Ctrl+Shift+P), start typing the **Python: Create Environment**
2. To select a specific environment, use the **Python: Select Interpreter** command from the Command Palette (Ctrl+Shift+P)



## Changing the execution policy of PowerShell

In order to corrently execute powershell files, you can set the execution policy by typing this into your PowerShell window (as an Administrator): 

`Set-ExecutionPolicy RemoteSigned`


For more information, see Using the Set-ExecutionPolicy Cmdlet.

When you are done, you can set the policy back to its default value with:

`Set-ExecutionPolicy Restricted`


You may see an error:

`Access to the registry key
'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PowerShell\1\ShellIds\Microsoft.PowerShell' is denied. 
To change the execution policy for the default (LocalMachine) scope, 
  start Windows PowerShell with the "Run as administrator" option. 
To change the execution policy for the current user, 
  run "Set-ExecutionPolicy -Scope CurrentUser".`


So you may need to run the command like this (as seen in comments):

`Set-ExecutionPolicy RemoteSigned -Scope CurrentUser`



Learn more: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies


## Requriements.txt File

When you're ready to deploy the application to other computers, you can create a `requirements.txt` file with the command `pip freeze > requirements.txt` (`pip3` on macOS/Linux). The requirements file describes the packages you've installed in your virtual environment. With only this file, you or other developers can restore those packages using `pip install -r requirements.txt` (or, again, `pip3` on macOS/Linux). By using a requirements file, you need not commit the virtual environment itself to source control.



## Use of the PYTHONPATH variable

An example of when to use PYTHONPATH would be if you have source code in a `src` folder and tests in a `tests` folder. When running tests, however, those tests can't normally access modules in `src` unless you hard-code relative paths.

To solve this problem, you could add the path to `src` to PYTHONPATH by creating an `.env` file within your VS Code workspace.

`PYTHONPATH=src`


Then set `python.envFile` in your `settings.json` file to point to the `.env` file you just created. For example, if the `.env` file was in your workspace root, your `settings.json` would be set as shown:

`"python.envFile": "${workspaceFolder}/.env"`


The value of PYTHONPATH can contain multiple locations separated by `os.pathsep`: a semicolon (;) on Windows and a colon (:) on Linux/macOS. 

Note: PYTHONPATH does **not** specify a path to a Python interpreter itself. For additional information about PYTHONPATH, read the PYTHONPATH documentation.


## Useful Extensions

Learn more: https://docs.python-guide.org/writing/structure/ 

Polyglot Notebooks: https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.dotnet-interactive-vscode 

Python Extension Template: https://code.visualstudio.com/api/advanced-topics/python-extension-template 

Azure Machine Learning: https://marketplace.visualstudio.com/items?itemName=ms-toolsai.vscode-ai 

GitHub Pull Requests and Issues: https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github 

GitHub Repositories: https://marketplace.visualstudio.com/items?itemName=github.remotehub

