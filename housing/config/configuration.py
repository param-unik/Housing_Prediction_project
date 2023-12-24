import sys
from housing.logger import logging
from housing.entity.config_entity import DataIngestionConfig, DataTransformConfig, DataValidationConfig, ModelTrainingConfig, ModelPusherConfig, \
    ModelEvaluationConfig, TrainingPipelineConfig
from housing.exception import HousingException
from housing.utils.common import read_yaml_file
from housing.constants import *


class Configuration:
    def __init__(
            self,
            config_file_path: CONFIG_FILE_PATH,
            current_time_stamp: CURRENT_TIME_STAMP
    ) -> None:
        try:
            self.config_info = read_yaml_file(config_file_path)
            self.training_pipeline_config = self.get_training_pipeline_config()
            self.time_stamp = current_time_stamp
            self.data_ingestion_config = self.get_data_ingestion_config()
            self.data_transform_config = self.get_data_transformation_config()
            self.data_validation_config = self.get_data_validation_config()
            self.model_training_config = self.get_model_trainer_config()
            self.model_pusher_config = self.get_model_pusher_config()

        except Exception as e:
            logging.info("Error occurred !")
            error = HousingException(e, sys)
            logging.error(error.error_message)

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        try:
            artifact_dir: str = self.training_pipeline_config.artifact_dir  # explicitly enforcing str
            data_ingestion_config = self.config_info[DATA_INGESTION_CONFIG_KEY]
            dataset_download_url = data_ingestion_config[DATA_INGESTION_DOWNLOAD_URL_KEY]

            data_ingestion_artifact_dir: str = os.path.join(artifact_dir, DATA_INGESTION_ARTIFACT_DIR, self.time_stamp) # explicitly enforcing str
            tgz_download_dir = os.path.join(data_ingestion_artifact_dir, data_ingestion_config[DATA_INGESTION_TGZ_DOWNLOAD_DIR_KEY])
            raw_data_dir = os.path.join(data_ingestion_artifact_dir, data_ingestion_config[DATA_INGESTION_RAW_DATA_DIR_KEY])
            ingested_data_dir = os.path.join(data_ingestion_artifact_dir, data_ingestion_config[DATA_INGESTION_INGESTED_DIR_NAME_KEY])
            ingested_test_dir = os.path.join(ingested_data_dir, data_ingestion_config[DATA_INGESTION_TEST_DIR_KEY])
            ingested_train_dir = os.path.join(ingested_data_dir, data_ingestion_config[DATA_INGESTION_TRAIN_DIR_KEY])

            data_ingestion_config = DataIngestionConfig(
                dataset_download_url=dataset_download_url,
                tgz_download_dir=tgz_download_dir,
                raw_data_dir=raw_data_dir,
                ingested_test_dir=ingested_test_dir,
                ingested_train_dir=ingested_train_dir
            )
            logging.info(f"Data Ingestion Config: {data_ingestion_config}")
            return data_ingestion_config
        except Exception as e:
            logging.info("Error occurred !")
            error = HousingException(e, sys)
            logging.error(error.error_message)

    def get_data_validation_config(self) -> DataValidationConfig:
        pass

    def get_data_transformation_config(self) -> DataTransformConfig:
        pass

    def get_model_trainer_config(self) -> ModelTrainingConfig:
        pass

    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        pass

    def get_model_pusher_config(self) -> ModelPusherConfig:
        pass

    def get_training_pipeline_config(self) -> TrainingPipelineConfig:
        try:
            training_pipeline_config = self.config_info[TRAINING_PIPELINE_CONFIG_KEY]
            pipeline_name = training_pipeline_config[TRAINING_PIPELINE_NAME_KEY]
            artifact_dir = os.path.join(ROOT_DIR, pipeline_name,
                                        training_pipeline_config[TRAINING_PIPELINE_ARTIFACT_DIR_KEY])
            training_pipeline_config = TrainingPipelineConfig(artifact_dir=artifact_dir,
                                                              pipeline_name=pipeline_name)
            logging.info("Training pipeline config: {}".format(training_pipeline_config))
            return training_pipeline_config
        except Exception as e:
            logging.info("Error occurred in get_training_pipeline_config() ")
            error = HousingException(e, sys)
            logging.error(error.error_message)
