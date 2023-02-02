# A simple  boilerplate template for Python in VsCode!

## Create virtual environment

1. Open the Command Palette (Ctrl+Shift+P), start typing the **Python: Create Environment**
2. To select a specific environment, use the **Python: Select Interpreter** command from the Command Palette (Ctrl+Shift+P)

Or use `create-venv.ps1` and `activate-venv.ps1` files. 


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


## Virtual Environments

You can give multiple directory arguments to create with a single command several virtual environments, into which you then install different sets of dependencies. `venv` can take a number of options:

|Option|Purpose|
|---|---|
|--clear|Removes any existing directory content before installing the virtual environment|
|--copies|Installs files by copying on the Unix-like platforms where using symbolic links is the default|
|--h or --help|Prints out a command-line summary and a list of available options|
|--system-site-packages|Adds the standard system site-packages directory to the environment’s search path, making modules already installed in the base Python available inside the environment|
|--symlinks|Installs files by using symbolic links on platforms where copying is the system default|
|--upgrade|Installs the running Python in the virtual environment, replacing whichever version the environment was created with|
|--without-pip|Inhibits the usual behavior of calling ensurepip to bootstrap the pip installer utility into the environment|


## Useful VsCode Extensions

Learn more: https://docs.python-guide.org/writing/structure/ 

Polyglot Notebooks: https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.dotnet-interactive-vscode 

Python Extension Template: https://code.visualstudio.com/api/advanced-topics/python-extension-template 

Azure Machine Learning: https://marketplace.visualstudio.com/items?itemName=ms-toolsai.vscode-ai 

GitHub Pull Requests and Issues: https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github 

GitHub Repositories: https://marketplace.visualstudio.com/items?itemName=github.remotehub

