from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .' 

def get_requirements(file: str) -> List[str]:
    '''
    Get requirements from file
    '''
    requirements=[]
    with open(file) as f:
        requirements = f.read().splitlines() #because slash also read
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)


setup(
name ='mlproject',
version='0.0.1',
author='Hajni Frecska',
author_email='frecskahajni@gmail.com',
package=find_packages(),
install_requires=get_requirements('requirements.txt')
)