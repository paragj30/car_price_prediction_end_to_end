from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'


def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [file.replace("\n","") for file in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name = "Car Price Prediction End to End Data Science",
    version = "0.0.1",
    author= "Parag Jadhav",
    author_email= "paragj30@gmail.com",
    packages= find_packages(),
    install_requires = get_requirements('requirements.txt')    

)