from src.exception import CustomException
from src.logger import logging
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from dataclasses import dataclass
import os,sys
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from src.utils import save_object
from src.utils import load_object
from src.components.data_ingestion import DataIngestion
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import numpy as np


@dataclass
class DataTransformationConfig:
    preprocessor_file_path = os.path.join("artifacts","preprocessor.pkl")

class DataTransform:
    def __init__(self):
        self.preprocessor_file = DataTransformationConfig()

    def get_data_transform_obj(self):

        try:

            logging.info("Data Transformation Started !!!! ")

            columns = ['id', 'diagnosis', 'radius_mean', 'texture_mean', 'perimeter_mean',
        'area_mean', 'smoothness_mean', 'compactness_mean', 'concavity_mean',
        'concave points_mean', 'symmetry_mean', 'fractal_dimension_mean',
        'radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se',
        'compactness_se', 'concavity_se', 'concave points_se', 'symmetry_se',
        'fractal_dimension_se', 'radius_worst', 'texture_worst',
        'perimeter_worst', 'area_worst', 'smoothness_worst',
        'compactness_worst', 'concavity_worst', 'concave points_worst',
        'symmetry_worst', 'fractal_dimension_worst']
            
            cat_features = ['diagnosis']
            num_features = ['id', 'radius_mean', 'texture_mean', 'perimeter_mean',
        'area_mean', 'smoothness_mean', 'compactness_mean', 'concavity_mean',
        'concave points_mean', 'symmetry_mean', 'fractal_dimension_mean',
        'radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se',
        'compactness_se', 'concavity_se', 'concave points_se', 'symmetry_se',
        'fractal_dimension_se', 'radius_worst', 'texture_worst',
        'perimeter_worst', 'area_worst', 'smoothness_worst',
        'compactness_worst', 'concavity_worst', 'concave points_worst',
        'symmetry_worst', 'fractal_dimension_worst']
            
            num_pipeline = Pipeline(
                steps=[("scaler",StandardScaler())]
            )

            transformer_obj = ColumnTransformer(
                [("num_pipeline",num_pipeline,num_features)]
            )

            logging.info("Sucessfully saved the preprocessor Object")

            return transformer_obj

    
        except Exception as e:
            raise CustomException(e,sys)
    
    def initiate_data_transform(self,train_path,test_path):

        try:
            encoder = LabelEncoder()
            preprocessor_obj = self.get_data_transform_obj()

            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            target_columns = ["diagnosis"]

            train_df_features = train_df.drop(target_columns,axis=1)
            train_target_column = train_df[target_columns]
            test_df_features = test_df.drop(target_columns,axis=1)
            test_target_column = test_df[target_columns]

            train_df_features = preprocessor_obj.fit_transform(train_df_features)
            train_target_column = encoder.fit_transform(train_target_column)
            test_df_features = preprocessor_obj.transform(test_df_features)
            test_target_column = encoder.transform(test_target_column)

            train_arr = np.c_[train_df_features,np.array(train_target_column)]
            test_arr = np.c_[test_df_features,np.array(test_target_column)]


            save_object(self.preprocessor_file.preprocessor_file_path,preprocessor_obj)
            return (train_arr,test_arr)

            
            
        except Exception as e:
            raise CustomException(e,sys)


        

        




        