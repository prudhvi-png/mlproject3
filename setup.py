from setuptools import setup, find_packages
import sys
from src.exception import CustomException


def install_requirements(file_path):
    try:
    
        with open(file_path, 'r') as file_obj:
            requirements = file_obj.readlines()
        
        requirements = [req.strip() for req in requirements]
        return requirements

    except Exception as e:
        raise CustomException(e,sys)

    




setup(
    name="Ml Project 3rd",
    version="0.0.1",
    author="prudhvi",
    author_email="prudhviredrouth143@gamil.com",
    packages=find_packages(),
    install_requires = install_requirements("requirements.txt")


)