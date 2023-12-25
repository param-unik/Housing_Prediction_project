import os
import sys
import tarfile

import numpy as np
import pandas as pd
from six.moves import urllib
from sklearn.model_selection import StratifiedShuffleSplit

from housing.entity.artifact_entity import DataIngestionArtifact
from housing.entity.config_entity import DataIngestionConfig
from housing.exception import HousingException
from housing.logger import logging


class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        try:
            logging.info(f"{'=' * 20} Data Ingestion Log started.. {'=' * 20} ")
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            logging.error("Error initializing DataIngestion")
            raise HousingException(e, sys)

    def download_input_data(self) -> str:
        try:
            # extracting remote url to download dataset
            download_url = self.data_ingestion_config.dataset_download_url

            # get the filename
            input_filename = os.path.basename(download_url)

            # folder location to download the file
            tgz_download_dir: str = self.data_ingestion_config.tgz_download_dir

            # check if a path exists and if it exists then removes it.
            if os.path.exists(tgz_download_dir):
                os.remove(tgz_download_dir)

            os.makedirs(tgz_download_dir, exist_ok=True)

            tgz_file_path: str = os.path.join(tgz_download_dir, input_filename)

            logging.info(f"Downloading {download_url} to {tgz_file_path} ...")

            # download the file from the download_url and place it in tgz_download_dir
            urllib.request.urlretrieve(download_url, tgz_file_path)

            logging.info(f"File {input_filename} has been download successfully!")

            return tgz_file_path

        except Exception as e:
            raise HousingException(e, sys)

    def extract_tgz_file(self, tgz_file_path: str) -> str:
        try:
            raw_data_dir = self.data_ingestion_config.raw_data_dir

            if os.path.exists(raw_data_dir):
                os.remove(raw_data_dir)

            os.makedirs(raw_data_dir, exist_ok=True)

            logging.info(
                f"File extracted successfully from {tgz_file_path} into {raw_data_dir}! "
            )
            with tarfile.open(tgz_file_path) as file_obj:
                file_obj.extractall(path=raw_data_dir)
            logging.info(f"File extracted successfully!! ")

            return raw_data_dir

        except Exception as e:
            raise HousingException(e, sys)

    def split_data_train_test_split(self) -> DataIngestionArtifact:
        try:
            raw_data_dir = self.data_ingestion_config.raw_data_dir
            file_name = os.listdir(raw_data_dir)[0]

            file_path = os.path.join(raw_data_dir, file_name)

            logging.info(f"Reading the csv file from {file_path}...")
            housing_df = pd.read_csv(file_path)

            housing_df["income_cat"] = pd.cut(
                housing_df["median_income"],
                bins=[0.0, 1.5, 3.0, 4.5, 6.0, np.inf],
                labels=[1, 2, 3, 4, 5],
            )

            strat_test_set = None
            strat_train_set = None

            logging.info(f"Splitting data into train and test set..")
            split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)

            for train_index, test_index in split.split(
                housing_df, housing_df["income_cat"]
            ):
                strat_train_set = housing_df.loc[train_index].drop(
                    ["income_cat"], axis=1
                )
                strat_test_set = housing_df.loc[test_index].drop(["income_cat"], axis=1)

            train_file_path = os.path.join(
                self.data_ingestion_config.ingested_train_dir, file_name
            )
            test_file_path = os.path.join(
                self.data_ingestion_config.ingested_test_dir, file_name
            )

            if strat_train_set is not None:
                os.makedirs(
                    self.data_ingestion_config.ingested_train_dir, exist_ok=True
                )
                strat_train_set.to_csv(train_file_path, index=False)
                logging.info("Saving training set data into {}".format(train_file_path))

            if strat_test_set is not None:
                os.makedirs(self.data_ingestion_config.ingested_test_dir, exist_ok=True)
                strat_test_set.to_csv(test_file_path, index=False)
                logging.info("Saving test set data into {}".format(test_file_path))

            data_ingestion_artifact = DataIngestionArtifact(
                train_file_path=train_file_path,
                test_file_path=test_file_path,
                is_ingested=True,
                message=f"Data Ingestion completed successfully!",
            )
            logging.info(
                "Data Ingestion completed successfully with details as {}".format(
                    data_ingestion_artifact
                )
            )

            return data_ingestion_artifact

        except Exception as e:
            raise HousingException(e, sys)

    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        try:
            tgz_file_path = self.download_input_data()
            self.extract_tgz_file(tgz_file_path=tgz_file_path)
            return self.split_data_train_test_split()

        except Exception as e:
            raise HousingException(e, sys)

    def __del__(self):
        logging.info(f"{'=' * 20} Data Ingestion log completed. {'=' * 20} \n")
