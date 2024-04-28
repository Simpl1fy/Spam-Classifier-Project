import os
import sys
import pandas as pd

from src.logger import logging
from src.exception import CustomException
from dataclasses import dataclass

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder

from src.utils import Stem, ToArray

@dataclass
class DataTransformationConfig:
    input_preprocessor_path:str = os.path.join('artifacts', 'preprocessor.pkl')


class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
    

    def get_data_transformation_object(self):
        try:
            independent_label = ['message']
            dependent = ['label']

            in_pipeline = Pipeline(
                steps=[
                    ("stemmer", Stem()),
                    ("cv", CountVectorizer(max_features=3000)),
                    ("to_array", ToArray())
                ]
            )

            le = LabelEncoder()

            

            return (
                in_pipeline,
                le
            )
            
        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_transformation(self, raw_data_path):
        logging.info('Initiating Data Transformation')
        try:
            logging.info('reading the data as a df')
            data = pd.read_csv(raw_data_path)



        except Exception as e:
            raise CustomException(e, sys)