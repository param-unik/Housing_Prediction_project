from housing.config.configuration import Configuration
from housing.logger import logging


def main():
    try:
        # pipeline = Pipeline()
        # pipeline.run_pipeline()

        # testing a validation process
        configuration = Configuration()
        data_validation_config = configuration.get_data_validation_config()
        # data_transformation_config = configuration.get_data_transformation_config()
        # print(data_transformation_config)
        print(data_validation_config)

    except Exception as e:
        logging.error(f"{e}")
        print(e)


if __name__ == "__main__":
    main()
