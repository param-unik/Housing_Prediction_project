from housing.config.configuration import Configuration
from housing.logger import logging
from housing.pipeline.pipeline import Pipeline
from housing.components.data_transformation import DataTransformation


def main():
    try:
        # pass
        # pipeline = Pipeline()
        # pipeline.run_pipeline()

        # testing a validation process
        # configuration = Configuration()
        # data_validation_config = configuration.get_data_validation_config()
        # data_transformation_config = configuration.get_data_transformation_config()
        # print(data_transformation_config)
        # print(data_validation_config)
        
        schema_file_path = r"/Users/paramjitsingh/Documents/GitHub/Housing_Prediction_project/config/schema.yaml"
        
        file_path = r"/Users/paramjitsingh/Documents/GitHub/Housing_Prediction_project/housing/artifact/data_ingestion/2023-12-25-19-37-58/ingested_data/train/housing.csv"
        
        df = DataTransformation.load_data(file_path = file_path, schema_file_path=schema_file_path)
        print(df.columns)
        print(df.dtypes)
        print(df.head())

    except Exception as e:
        logging.error(f"{e}")
        print(e)


if __name__ == "__main__":
    main()
