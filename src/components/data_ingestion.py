import os
import sys
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.logger import logging
import pandas as pd
from src.exception import CustomException
from data_transformation import DataTransform
from model_trainer import ModelTrainer



@dataclass
class DataIngestionConfig:

    train_data_file_path = os.path.join("artifacts",'train_df.csv')
    test_data_file_path = os.path.join("artifacts","test_df.csv")
    raw_data_file_path = os.path.join("artifacts","raw.csv")

class DataIngestion:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        try:

            logging.info("Data Ingestion Started !!!!! ")

            os.makedirs(os.path.dirname(self.data_ingestion_config.raw_data_file_path),exist_ok=True)

            df = pd.read_csv("Project3\\notebooks\\data\\cancer.csv")

            df.to_csv(self.data_ingestion_config.raw_data_file_path,index=False,header=True)

            train_set,test_set = train_test_split(df,test_size=0.3,random_state=42)

            logging.info("Successfully completed train test split")

            train_set.to_csv(self.data_ingestion_config.train_data_file_path,index=False,header=True)

            test_set.to_csv(self.data_ingestion_config.test_data_file_path,index=False,header=True)

            logging.info("Sucessfully completed the Data set Ingestion !!!!")

            return (
                self.data_ingestion_config.train_data_file_path,
                self.data_ingestion_config.test_data_file_path
            )
        
        except Exception as e:
            raise CustomException(e,sys)
        

if __name__ == "__main__":
    data_ingestion_obj = DataIngestion()

    train_df,test_df = data_ingestion_obj.initiate_data_ingestion()
    
    data_transform_obj = DataTransform()
    file_path = data_transform_obj.get_data_transform_obj()
    train_arr,test_arr = data_transform_obj.initiate_data_transform(train_df,test_df)
    model_trainer = ModelTrainer()
    model,accuracy = model_trainer.initiate_model_training(train_arr,test_arr)
    print(model)
    print(accuracy)
    




