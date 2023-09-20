from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = '-e .'

def find_libraries(requirement_file: str) -> List[str]:
    
    requirements = []

    with open(requirement_file) as file_obj:
        requirements = file_obj.readlines()
        requirements = [i.replace('\n','') for i in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name='mlproject',
    version='1.0',
    description="Machine Learning Project",
    author="Dev Faisal",
    packages=find_packages(),
    install_requires=find_libraries("requirements.txt"),
)