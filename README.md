# gitterPy 
## EML Git Automation Script
This Python script automates the process of committing and pushing changes to a Git repository or running pytest in a more streamlined manner.

## Prerequisites
- Python 3.x
- Package installer lib 'pip'
- Any git repository

## Usage
- To use this script, simply place it in the git repository's parent folder (where you can find a folder named .git) 

     - .git is a hidden folder; so you may need to unhide files first; or run the following commands and search for .git  
        (MAC/Linux)  
        `ls -a`  
        (Windows)   
        `dir /a`

- Run gitterpy with the appropriate argument. For example, to run pytest (to evaluate your work locally), use the following command:

    `python gitterpy.py test`

- To (submit) commit and push changes to the remote Git repository, use the following command:

    `python gitterpy.py upload`

If any errors occur during the push, the script will print an error message.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License - see the [LICENSE.md](./LICENSE.md) file for details.