from setuptools import find_packages,setup
from typing import List

HYPHEN = '-e .'

def get_requirements(file_path:str)->List[str]:

  """
    returns list of requirements
  """

  requirements = []

  with open(file_path) as f:
    requirements = f.readlines()
    requirements = [req.replace('\n', '') for req in requirements]

    if HYPHEN in requirements:
      requirements.remove(HYPHEN)

  return requirements
    




setup(
    name = 'mlproject'
    ,version = '0.0.1'
    ,author = 'ankan datta'
    ,packages = find_packages()
    ,install_requires = get_requirements('requirements.txt')
)