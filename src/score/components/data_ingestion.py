import os                # Importing the os module for operating system dependent functionality
import sys               # Importing the sys module for system-specific parameters and functions
from src.score.exception import CustomException   # Importing CustomException class from src.score.exception module
from src.score.logger import logging              # Importing logging object from src.score.logger module
import pandas as pd                               # Importing pandas library and aliasing it as pd
from src.score.utils import read_sql_data         # Importing read_sql_data function from src.score.utils module
from sklearn.model_selection import train_test_split  # Importing train_test_split function from sklearn.model_selection module
from dataclasses import dataclass                 # Importing dataclass decorator from dataclasses module

'''
A data class in Python is a class typically used for storing data. 
It is created using the dataclass decorator provided by the dataclasses module, introduced in Python 3.7. 
Data classes reduce boilerplate code by automatically generating special methods such as __init__, __repr__, __eq__, and __hash__ based on the class attributes. 
They are mainly used for representing simple objects with a fixed set of attributes.
'''
@dataclass                     # Decorator to convert class into a data class
class DataIngestionConfig:
    train_data_path:str=os.path.join('artifacts','train.csv')   # Default path for training data CSV file
    test_data_path:str=os.path.join('artifacts','test.csv')     # Default path for testing data CSV file
    raw_data_path:str=os.path.join('artifacts','raw.csv')       # Default path for raw data CSV file

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()     # Initializing DataIngestionConfig object

    def initiate_data_ingestion(self):
        try:
            df=read_sql_data()
            # df=pd.read_csv(os.path.join('notebook/data','raw.csv')) 
            #  Reading raw data from CSV file into a DataFrame
            logging.info("Reading completed from mysql database")          # Logging info message

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)   # Creating directory if it doesn't exist

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)   # Writing raw data to CSV file
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)   # Splitting data into train and test sets
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)   # Writing train set to CSV file
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)     # Writing test set to CSV file

            logging.info("Data Ingestion is completed")   # Logging info message

            return (
                self.ingestion_config.train_data_path,    # Returning path of the train data CSV file
                self.ingestion_config.test_data_path      # Returning path of the test data CSV file
            )

        except Exception as e:
            raise CustomException(e,sys)   # Raising CustomException in case of any exception
