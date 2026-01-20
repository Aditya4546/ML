from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirments(file_path:str) -> list[str]:
    '''
    retun list of req
    '''
    req =[]
    with open(file_path) as file:
        req = file.readlines()
        [rq.replace("\n", "") for rq in  req ]
        if HYPHEN_E_DOT in req:
            req.remove(HYPHEN_E_DOT)

    return req

setup(name= 'ML' , 
      version='0.0.1',
      author='Aditya',
      author_email='adityarenke92@gmail.com',
      packages=find_packages(),
      install_requires= get_requirments('requirements.txt'),

      )


