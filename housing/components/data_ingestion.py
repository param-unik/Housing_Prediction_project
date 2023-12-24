import os
import sys

from housing.entity.config_entity import DataIngestionConfig
from housing.exception import HousingException
from housing.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass


class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        try:
            logging.info(f"{'=' * 20} Data Ingestion Log started.. {'=' * 20} ")
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            logging.error("Error initializing DataIngestion")
            raise HousingException(e, sys)


    def initialize_data_ingestion(self) -> DataIngestionArtifact:
        try:
            pass
        except Exception as e:
            raise HousingException(e, sys)




