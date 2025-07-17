from src.exception import CustomException
from src.logger import logging
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from dataclasses import dataclass
import os,sys
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from src.utils import save_object


@dataclass
class DataTransformationConfig:
    preprocessor_file_path = os.path.join("artifacts","preprocessor.pkl")

class DataTransform:
    def __init__(self):
        self.preprocessor_file = DataTransformationConfig()

    def get_data_transform_obj(self,train_df,test_df):

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
            cat_pipeline = Pipeline(
                steps=[("encoder",OneHotEncoder(sparse_output=False)),
                    ("scaler",StandardScaler())]
            )

            transformer_obj = ColumnTransformer(
                [("num_pipeline",num_pipeline,num_features),
                ("cat_features",cat_pipeline,cat_features)]
            )

            save_object(
                self.preprocessor_file.preprocessor_file_path,
                transformer_obj
            )
            
            save_object(
                file_path=self.preprocessor_file.preprocessor_file_path,
                obj=transformer_obj
            )
            logging.info("Sucessfully saved the preprocessor Object")


        except Exception as e:
            raise CustomException(e,sys)
        

        




        