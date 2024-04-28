from flask import Flask,request,render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.Car_Price_Prediction_Data_Science.pipelines.prediction_pipeline import CustomData,PredictPipeline

from src.Car_Price_Prediction_Data_Science.logger import logging
from src.Car_Price_Prediction_Data_Science.exception import CustomException
import sys
from src.Car_Price_Prediction_Data_Science.components.data_ingestion import DataIngestion

from src.Car_Price_Prediction_Data_Science.components.data_transformation import DataTransformationConfig, DataTransformation
from src.Car_Price_Prediction_Data_Science.components.model_training import ModelTrainerConfig, ModelTrainer

application=Flask(__name__)

app=application

## Route for a home page

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        data=CustomData(
            Make=request.form.get('Make'),
            Model=request.form.get('Model'),
            Year=request.form.get('Year'),
            Engine_Fuel_Type=request.form.get('Engine_Fuel_Type'),
            Engine_HP=request.form.get('Engine_HP'),
            Engine_Cylinders=request.form.get('Engine_Cylinders'),
            Transmission_Type=request.form.get('Transmission_Type'),
            Driven_Wheels=request.form.get('Driven_Wheels'),
            Number_of_Doors=request.form.get('Number_of_Doors'),
            Market_Category=request.form.get('Market_Category'),
            Vehicle_Size=request.form.get('Vehicle_Size'),
            Vehicle_Style=request.form.get('Vehicle_Style'),
            highway_MPG=request.form.get('highway_MPG'),
            city_mpg=request.form.get('city_mpg'),
            Popularity=request.form.get('Popularity'),

        )
        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline=PredictPipeline()
        print("Mid Prediction")
        results=predict_pipeline.predict(pred_df)
        print("after Prediction")
        return render_template('home.html',results=results[0])
    

if __name__=="__main__":
    app.run(host="0.0.0.0")        