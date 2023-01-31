# dev_django

To install the dependencies listed in a "requirements.txt" file in a Django project, you can use the pip (Python Package Manager) package manager. Here are the steps to install the dependencies:

1) Open a terminal or command prompt in the project directory.
2) Activate the virtual environment for the project, if you have one.
3) Run the following command: "pip install -r requirements.txt".

This command will read the "requirements.txt" file and install all the dependencies listed in it. The installed packages will be stored in the virtual environment's site-packages directory.

If you add or remove dependencies in the future, you can update the "requirements.txt" file and run the "pip install -r requirements.txt" command again to install the updated dependencies. If you install a new package using the "pip install <package_name>" command, you can add it to the "requirements.txt" file by running "pip freeze > requirements.txt".
