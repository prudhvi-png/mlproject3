import os
from src.exception import CustomException
from datetime import datetime
import logging
import sys


try:

    logs_dir = os.path.join(os.getcwd(),"Logs")

    os.makedirs(logs_dir,exist_ok=True)

    log_name = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

    log_path = os.path.join(logs_dir,log_name)

    logging.basicConfig(
        filename=log_path,
        level=logging.INFO,
        format='[%(asctime)s] %(levelname)s - %(message)s',
    )
except Exception as e:
    raise CustomException(e,sys)


