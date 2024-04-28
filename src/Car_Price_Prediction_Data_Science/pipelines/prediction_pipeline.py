import sys
import os
import pandas as pd
from src.Car_Price_Prediction_Data_Science.exception import CustomException
from src.Car_Price_Prediction_Data_Science.utils import save_object, load_object

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)

class CustomData:
    def __init__(self,
                 Make: str,
                 Model: str,
                 Year: int,
                 Engine_Fuel_Type: str,
                 Engine_HP: int,
                 Engine_Cylinders: int,
                 Transmission_Type: str,
                 Driven_Wheels: str,
                 Number_of_Doors: int,
                 Market_Category: str,
                 Vehicle_Size: str,
                 Vehicle_Style: str,
                 highway_MPG: int,
                 city_mpg: int,
                 Popularity: int
                 ):
        self.Make = Make

        self.Model = Model

        self.Year = Year

        self.Engine_Fuel_Type = Engine_Fuel_Type

        self.Engine_HP = Engine_HP

        self.Engine_Cylinders = Engine_Cylinders

        self.Transmission_Type = Transmission_Type

        self.Driven_Wheels = Driven_Wheels

        self.Number_of_Doors = Number_of_Doors

        self.Market_Category = Market_Category
    
        self.Vehicle_Size = Vehicle_Size

        self.Vehicle_Style = Vehicle_Style

        self.highway_MPG = highway_MPG

        self.city_mpg = city_mpg

        self.Popularity = Popularity

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "Make": [self.Make],
                "Model": [self.Model],
                "Year": [self.Year],
                "Engine_Fuel_Type": [self.Engine_Fuel_Type],
                "Engine_HP": [self.Engine_HP],
                "Engine_Cylinders": [self.Engine_Cylinders],
                "Transmission_Type": [self.Transmission_Type],
                "Driven_Wheels": [self.Driven_Wheels],
                "Number_of_Doors": [self.Number_of_Doors],
                "Market_Category": [self.Market_Category],
                "Vehicle_Size": [self.Vehicle_Size],
                "Vehicle_Style": [self.Vehicle_Style],
                "highway_MPG": [self.highway_MPG],
                "city_mpg": [self.city_mpg],
                "Popularity": [self.Popularity],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)
