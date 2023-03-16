# The following packages are called 'standard library packages' as they are included with python
# Have a look at https://docs.python.org/3/library/index.html for info on standard lib packages.
import os
import pip
import sys
import platform

# Define a function to check whether a required package is installed
# If it isn't installed, use pip to install it
def import_or_install(package):
    try:
        __import__(package)
    except ImportError:
        pip.main(['install', package])

# Check whether the GitPython and pytest packages are installed
# If not, install them
import_or_install('GitPython')
import_or_install('pytest')

# Import necessary modules
from git import Repo
from datetime import datetime

# Assign the current date and time to the 'timestamp' variable
timestamp = datetime.now()

# Set the path of the Git repository directory
# By default it is the same directory as your .git folder
PATH_OF_GIT_REPO = r'.git'

# Create a commit message that includes the current timestamp
COMMIT_MESSAGE = 'py commit @ ' + timestamp.strftime('%x-%X')

# lambda func to ret splitting lines, def arg is 0
retLine = lambda err=0 : '\n'+'!'*100+'\n' if err else '\n'+'='*100+'\n'

# Define a function to push changes to the remote Git repository
def git_push():
    try:
        # Use GitPython to add and commit changes
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add(update=True)
        repo.index.commit(COMMIT_MESSAGE)
        # Use GitPython to push changes to the remote repository
        origin = repo.remote(name='origin')
        origin.push()
    except Exception:
        # Print an error message if an error occurs during the push
        print(retLine(1) + 'Some error occured while pushing the code.\nContact the instructor with a screenshot of message\n' + Exception + retLine(1))
        
    else:
        print("Yay! Successfully uploaded" + retLine())

# Check the value of the first argument passed to the script
if sys.argv[1]=='test':

    # If the platform is Linux or macOS, use 'python3 -m pytest' to run pytest
    if platform.system() == "Linux" or platform.system() == "Darwin":
        os.system("python3 -m pytest")
    
    # If the platform is Windows, use 'pytest' to run pytest
    elif platform.system() == "Windows":
        os.system("pytest")

    else:
        raise Exception(retLine(1) + "You must be running some fancy OS. Contact the instructor with a screenshot of message\n" + platform.system() + retLine(1))

# If the first argument is 'upload', call the 'git_push()' function to push changes to the remote repository
elif sys.argv[1]=='upload':
    git_push()
