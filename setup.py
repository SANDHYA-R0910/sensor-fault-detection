from setuptools import find_packages,setup
from typing import list

def get_requirements()->List[str]:
    """
    This function will return a list of requirements
    
    """
    requirement_list: List[str] = []
    
    with open('requirements.txt','r') as f:
        for i in f:
            requirement_list.append(i.strip())
            
    return requirement_list
    

setup(
    name="sensor",
    version="0.0.1",
    author="sandhya",
    author_email="sandhyarsanju@gmail.com",
    packages = find_packages(),
    install_requires=get_requirements(),#["pymongo==4.2.0"],
)