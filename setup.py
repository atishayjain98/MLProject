from setuptools import setup, find_packages
from typing import List

Hyphen_E_dot = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements.
    '''
    
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readline()
        requirements = [req.replace("/n", "") for req in requirements]
        
        if Hyphen_E_dot in requirements:
            requirements.remove(Hyphen_E_dot)
        
    return requirements 

setup(
    name='ML Project',
    version=0.1,
    author='Atishay Jain',
    author_email='atishayjainnew@gmail.com',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt')
)
