#-> Create a project template to maintain a folder structure and provide a wireframe to the Project Flow.
  # -- This is a one time effort, it can be created using AWS SAM command


import os
from pathlib import Path
import logging 

#logging string: To log every step of the process

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = 'cnnClassifier'


list_of_files = [
    ".github/workflows/.gitkeep", #File to keep as a placeholder, if no file is to be uploaded
    f"src/{project_name}/components/__init__.py", #Used Source (src) file path, so that whenever we need to add any file to a particular folder inside the source project, it can be done easily, directing via 'src'
    f"src/{project_name}/utils/__init__.py", #__init__ is installed as a contructor file inside every folder
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuratuion.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb",
    "templates/index.html"
    # Add Files to be utilized in this project

]

# FOR Loop Code to create the list of files
for filepath in list_of_files: #Using for loop to scan through each file in the list
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath) #To split the folder name and file name from the path

    if filedir != "":
        os.makedirs(filedir, exist_ok=True) #'makedirs' function to create directory
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

   # Condition to make sure if the filepath (filename) doesn't exist or the size is 0, then only create the file
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): 
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    
    else:
        logging.info(f"{filename} already exists")



