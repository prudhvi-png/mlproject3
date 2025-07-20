from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from dataclasses import dataclass
import os
import sys
from src.exception import CustomException
from src.logger import logging
from src.utils import save_object
from sklearn.metrics import accuracy_score,recall_score
from src.utils import save_info


@dataclass
class ModelTrainerConfig:
    model_file_path = os.path.join("artifacts","model.pkl")
    model_info_path = os.path.join("artifacts","outputs.txt")


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def evaluate_model(self,true,predicted):
        try:
            acc_score = accuracy_score(true,predicted)
            re_score = recall_score(true,predicted)
            return acc_score,re_score
        except Exception as e:
            raise CustomException(e,sys)
    
    def initiate_model_training(self,train_arr,test_arr):
        try:

            models = {
                "LogisticRegression" : LogisticRegression(),
                "DecisionTreeClassifier" : DecisionTreeClassifier(),
                "SVC" : SVC(),
                "RandomForestClassifier" : RandomForestClassifier(),
                "KNeighborsClassifier" : KNeighborsClassifier()
            }
            
            x_train = train_arr[:,:-1]
            y_train = train_arr[:,-1]
            x_test = test_arr[:,:-1]
            y_test = test_arr[:,-1]

            best_acc_score = 0
            best_model = None

            for name,model in models.items():
                model.fit(x_train,y_train)

                y_test_pred = model.predict(x_test)

                acc_score,re_score = self.evaluate_model(y_test,y_test_pred)

                if acc_score > best_acc_score:
                    best_acc_score = acc_score
                    best_model = model
                logging.info("best model found ")

            save_object(self.model_trainer_config.model_file_path,best_model)
            save_info(model_name=best_model,file_path=self.model_trainer_config.model_info_path,best_score=best_acc_score)

            return (best_model,best_acc_score)
        except Exception as e:
            raise CustomException(e,sys)
