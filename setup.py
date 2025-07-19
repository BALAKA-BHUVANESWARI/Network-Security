'''
The setup.py file is an essential part of packagingand distributing python projects.and.and.it is used by setuptools
to define teh configuration of your projects such as its metadata,dependencies and more'''



from setuptools import find_packages,setup
from typing import List

def get_requirements():
    """
    this function will return list of requirements
    """

    requirement_lst=[]
    try:
        with open('requirements.txt','r') as file:
            #Read lines from the file
            lines=file.readlines()
            #process the line
            for line in lines:
                requirement=line.strip()
                #ignore empty lines and -e
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")
    return requirement_lst
setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="bhanu",
    author_email="bhanubalaka@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)



