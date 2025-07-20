from src.exception import CustomException
from src.logger import logging
import os,sys
import dill
from sklearn.metrics import accuracy_score,recall_score


def save_object(file_path,obj):
    try:
        
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_path)

    except Exception as e:
        raise CustomException(e,sys)
    
def load_object(file_path):
    try:
        with open(file_path,'rb') as file_obj:
            return dill.load(file_obj)
    except Exception as e:
        raise CustomException(e,sys)
    
def save_info(model_name,file_path,best_score):
    try:
        with open(file_path,'w') as file_obj:
            file_obj.write(f"The winner is {model_name} with best score of {best_score}")
            file_obj.close()
    except Exception as e:
        raise CustomException(e,sys)

