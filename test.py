from src.logger import logging
from src.exception import CustomException
import sys



try:
    logging.info("Logging Started")
    print(1/0)
except Exception as e:
    raise CustomException(e,sys)
    