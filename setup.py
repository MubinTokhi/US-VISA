from setuptools import setup, find_packages
from typing import List


HYPEN_E_DOT = '-e .'
def get_requirements(file_path: str) -> List[str]:
    """
    This function will return the list of requirments
    """
    requirements = []
    with open (file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements= [i.replace("\n","") for i in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements





setup(
    name="us_visa",
    version= "0.0.0",
    author = "Mubin Ahmad",
    author_email= "mobin.khan.amiri@gmail.com",
    packages=find_packages(where='us_visa'),
    install_requires=get_requirements("requirements.txt")
)