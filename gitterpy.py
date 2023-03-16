# The following packages are called 'standard library packages' as they are included with python
# Have a look at https://docs.python.org/3/library/index.html for info on standard lib packages.
import pip
import sys
import platform
import datetime
import subprocess
import traceback

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

# Import after checking installation
from git import Repo

# Assign the current date and time to the 'timestamp' variable
timestamp = datetime.datetime.now()

# Set the path of the Git repository directory
# By default it is the same directory as your .git folder
PATH_OF_GIT_REPO = r'.git'

# Create a commit message that includes the current timestamp
COMMIT_MESSAGE = 'py commit @ ' + timestamp.strftime('%x-%X')

# print with colors for CLI outputs 
def wrapOutput(errFlag, str):
    if errFlag:
        print('!'*100 + '\n\033[38;5;197m' + str + '\033[0;0m\n' + '!'*100)
    else:
        print('='*100 + '\n\033[38;5;119m' + str + '\033[0;0m\n' + '='*100)

def run_pytest(cmd):
    try:
        # Use subprocess to run the pytest command
        subprocess.run(cmd)
    except subprocess.CalledProcessError:
        # Print an error message if an error occurs during the pytest run
        wrapOutput(1, ' Some error occured while running pytest. Contact the instructor with a screenshot of message\n' + traceback.format_exc())

# Define a function to push changes to the remote Git repository
def git_push():
    try:
        # Use GitPython to add and commit changes
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add(update=True)
        repo.index.commit(COMMIT_MESSAGE)
        # Use GitPython to push changes to the remote repository
        origin = repo.remote(name='origin')
        origin.pull()
        origin.push()
    except Exception:
        # Print an error message if an error occurs during the push
        wrapOutput(1, 'Some error occured while pushing the code.\nContact the instructor with a screenshot of message\n' + Exception)
    else:
        wrapOutput(0, 'Yay! Successfully uploaded')

# Check the value of the first argument passed to the script
if sys.argv[1]=='test':

    # If the platform is Linux or macOS, use 'python3 -m pytest' to run pytest
    if platform.system() == 'Linux' or platform.system() == 'Darwin':
        run_pytest('python3 -m pytest')
    
    # If the platform is Windows, use 'pytest' to run pytest
    elif platform.system() == 'Windows':
        run_pytest('pytest')

    else:
        wrapOutput(1, 'You must be running some fancy OS. Contact the instructor with a screenshot of message\n' + platform.system())

# If the first argument is 'upload', call the 'git_push()' function to push changes to the remote repository
elif sys.argv[1]=='upload':
    git_push()
