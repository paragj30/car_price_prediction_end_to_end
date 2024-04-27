from src.Car_Price_Prediction_Data_Science.logger import logging
from src.Car_Price_Prediction_Data_Science.exception import CustomException
import sys
from src.Car_Price_Prediction_Data_Science.components.data_ingestion import DataIngestion

from src.Car_Price_Prediction_Data_Science.components.data_transformation import DataTransformationConfig, DataTransformation


if __name__ == "__main__":
    logging.info('Testing_1: The execution has started')
    try:
        data_ingestion = DataIngestion()
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()
        #data_transformation_config = DataTransformationConfig()
        data_transformation = DataTransformation()
        data_transformation.initiate_data_transormation(train_data_path, test_data_path)


    except Exception as e:
        logging.info('Custom Exception')
        raise CustomException(e, sys)