import os  # Importing the os module to interact with the operating system.
from pathlib import Path  # type: ignore # Importing Path class from pathlib module for path manipulation.
import logging  # Importing logging module for logging events and messages.

logging.basicConfig(level=logging.INFO)  # Configuring the logging module to display INFO level messages.

project_name="score"  # Defining the name of the project.

# List of files to be created or checked for existence.
list_of_files=[
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_monitoring.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/training_pipeline.py",
    f"src/{project_name}/pipelines/prediction_pipeline.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py"
]

# Iterating through each filepath in the list of files.
for filepath in list_of_files:
    filepath = Path(filepath)  # Converting the filepath to a Path object for easier manipulation.
    filedir, filename = os.path.split(filepath)  # Splitting the filepath into directory and filename.

    # Checking if directory part of filepath is not empty.
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)  # Creating directory if it doesn't exist.
        logging.info(f"Creating directory:{filedir} for the file {filename}")  # Logging the creation of directory.

    # Checking if the file doesn't exist or is empty.
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:  # Opening the file in write mode.
            pass  # Doing nothing as we are just creating an empty file.
        logging.info(f"Creating empty file: {filepath}")  # Logging the creation of an empty file.

    else:
        logging.info(f"{filename} is already exists")  # Logging if the file already exists.
