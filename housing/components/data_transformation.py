import sys

import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

from housing.constants import *
from housing.entity.artifact_entity import DataValidationArtifact
from housing.entity.config_entity import DataTransformConfig, DataIngestionConfig
from housing.exception import HousingException
from housing.utils.common import read_yaml_file


class FeatureGenerator(BaseEstimator, TransformerMixin):
    def __init__(
        self,
        add_bedrooms_per_room=True,
        total_rooms_ix=3,
        population_ix=5,
        household_ix=6,
        total_bedrooms_ix=4,
        columns=None,
    ):
        try:
            self.columns = columns
            if self.columns is not None:
                total_rooms_ix = self.columns.index(COLUMN_TOTAL_ROOMS)
                population_ix = self.columns.index(COLUMN_POPULATION)
                household_ix = self.columns.index(COLUMN_HOUSEHOLDS)
                total_bedrooms_ix = self.columns.index(COLUMN_TOTAL_BEDROOM)
            self.add_bedrooms_per_room = add_bedrooms_per_room
            self.total_rooms_ix = total_rooms_ix
            self.population_ix = population_ix
            self.household_ix = household_ix
            self.total_bedrooms_ix = total_bedrooms_ix

        except Exception as e:
            raise HousingException(e, sys)

    def fit(self, x, y=None):
        return self

    def transform(self, x, y=None):
        try:
            room_per_household = x[:, self.total_rooms_ix] / x[:, self.household_ix]
            population_per_household = (
                x[:, self.population_ix] / x[:, self.household_ix]
            )

            if self.add_bedrooms_per_room:
                bedrooms_per_room = (
                    x[:, self.total_bedrooms_ix] / x[:, self.total_rooms_ix]
                )
                generated_feature = np.c_[
                    x, room_per_household, population_per_household, bedrooms_per_room
                ]
            else:
                generated_feature = np.c_[
                    x, room_per_household, population_per_household
                ]
            return generated_feature
        except Exception as e:
            raise HousingException(e, sys)


class DataTransformation:
    def __init__(
        self,
        data_transform_config: DataTransformConfig,
        data_ingestion_config: DataIngestionConfig,
        data_validation_artifact: DataValidationArtifact,
    ):
        try:
            self.data_transform_config = data_transform_config
            self.data_ingestion_config = data_ingestion_config
            self.data_validation_artifact = data_validation_artifact
        except Exception as e:
            raise HousingException(e, sys)

    def load_data(self, file_path: str, schema_file_path: str) -> pd.DataFrame:
        try:
            dataset_schema = read_yaml_file(schema_file_path)
        except Exception as e:
            raise HousingException(e, sys)
