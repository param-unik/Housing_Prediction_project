from setuptools import setup, find_packages

PROJECT_NAME = 'housing-predictor'
PROJECT_DESCRIPTION = 'This is ML project for ML for regression problem'
AUTHOR = 'Paramjit'
AUTHOR_EMAIL = 'param-unik@gmail.com'
PACKAGES = ["housing"]
VERSION = "0.0.1"
REQUIREMENT_FILE = "requirements.txt"


def get_requirements_list():

    """
    Function to get the requirement list from requirements.txt

    :return: List of requirement packages which needs to be installed

    """
    with open(REQUIREMENT_FILE, "r") as file:
        requirements = [req.replace("\n", "") for req in file.readlines()]
        requirements.remove('-e .')
    return requirements


setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=PROJECT_DESCRIPTION,
    packages=PACKAGES,
    install_requires=get_requirements_list()
)
