from src.Car_Price_Prediction_Data_Science.logger import logging
from src.Car_Price_Prediction_Data_Science.exception import CustomException
import sys
from src.Car_Price_Prediction_Data_Science.components.data_ingestion import DataIngestion

if __name__ == "__main__":
    logging.info('Testing_1: The execution has started')

    try:
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()

    except Exception as e:
        logging.info('Testing_2: Checking the Custom Exception Error code block working')
        raise CustomException(e, sys)