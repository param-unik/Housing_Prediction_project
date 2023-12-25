import sys

from housing.components.data_ingestion import DataIngestion
from housing.config.configuration import Configuration
from housing.constants import *
from housing.entity.artifact_entity import (
    DataIngestionArtifact,
    DataValidationArtifact,
    DataTransformationArtifact,
    ModelTrainerArtifact,
    ModelEvaluationArtifact,
    ModelPusherArtifact,
)
from housing.exception import HousingException
from housing.logger import logging


class Pipeline:
    def __init__(
        self,
        config: Configuration = Configuration(
            config_file_path=CONFIG_FILE_PATH, current_time_stamp=CURRENT_TIME_STAMP
        ),
    ):
        try:
            self.config = config
        except Exception as e:
            raise HousingException(e, sys)

    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            data_ingestion_config = self.config.get_data_ingestion_config()
            data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
            return data_ingestion.initiate_data_ingestion()
        except Exception as e:
            raise HousingException(e, sys)

    def start_data_validation(self) -> DataValidationArtifact:
        pass

    def start_data_transformation(self) -> DataTransformationArtifact:
        pass

    def start_model_trainer(self) -> ModelTrainerArtifact:
        pass

    def start_model_evaluation(self) -> ModelEvaluationArtifact:
        pass

    def start_model_pusher(self) -> ModelPusherArtifact:
        pass

    def run_pipeline(self):
        try:
            # data ingestion
            logging.info(f"Run Pipeline started here for data ingestion....")
            data_ingestion_artifact = self.start_data_ingestion()
            logging.info(f"Run Pipeline ended here for data ingestion...")
        except Exception as e:
            raise HousingException(e, sys)
