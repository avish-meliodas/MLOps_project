from mlproject.config.configuration import ConfigurationManager
from mlproject.components.data_transformation import DataTransformation
from mlproject import logger

STAGE_NAME = "Data Transform stage"

class DataTransformationTrainingPipeline:

    def __init__(self):
        pass


    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(data_transformation_config)
        data_transformation.test_train_spliting()


if __name__ == "__main__":

    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<")
    except Exception as e:
        logger.exception(e)