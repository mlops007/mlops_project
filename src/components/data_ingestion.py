import os
import sys
from src.exception import CustomException
from src.logger import logging
from sklearn.model_selection import train_test_split
import pandas as pd
from dataclasses import dataclass
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig


@dataclass
class DatsIngestionConfig:
    train_data_path : str = os.path.join('artifacts', 'train.csv')
    test_data_path : str = os.path.join('artifacts', 'test.csv')
    raw_data_path : str = os.path.join('artifacts', 'raw.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config=(DatsIngestionConfig)

    def iniitiate_data_ingestion(self):
        logging.info('Entry into Data Ingestion methood')
        try:
            df = pd.read_csv('notebooks\data\StudentsPerformance.csv')
            logging.info('Read the dataset as pandas dataframe')
            df['total_score'] = df['math score'] + df['reading score'] + df['writing score']
            df['average'] = df['total_score']/3
            logging.info('Did minor transformations')
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok = True)
            os.makedirs(os.path.dirname(self.ingestion_config.test_data_path), exist_ok = True)
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok = True)

            df.to_csv(self.ingestion_config.raw_data_path, index = False, header= True)

            logging.info('Train Test Split Initiated')

            train_set, test_set = train_test_split(df, test_size = 0.2, random_state = 100)
            df.to_csv(self.ingestion_config.train_data_path, index = False, header= True)
            df.to_csv(self.ingestion_config.test_data_path, index = False, header= True)

            logging.info('Ingestion Complete')
            
            return(
                self.ingestion_config.train_data_path
                ,self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e, sys)
        
if __name__ == '__main__':
    
    obj = DataIngestion()
    train_data, test_data = obj.iniitiate_data_ingestion()

    data_transformation = DataTransformation()
    data_transformation.initiate_data_transformation(train_data, test_data)