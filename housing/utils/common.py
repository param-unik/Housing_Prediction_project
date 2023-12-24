import sys
import yaml

from housing.exception import HousingException
from housing.logger import logging


def read_yaml_file(file_path: str) -> dict:
    """
    Read YAML file and return contents as a dictionary
    :param
        file_path: str
    :return: ConfigBox
    """

    try:
        with open(file_path, 'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        housing_error = HousingException(e, sys)
        logging.info(housing_error.error_message)
