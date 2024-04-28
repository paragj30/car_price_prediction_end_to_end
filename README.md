# End to end Car Price Prediction Data Science Project - Parag Jadhav 

### Introduction About the Data :

**The dataset** The goal is to predict `MSRP` of given vehicle (Regression Analysis).

There are 16 independent variables:

* `Make` : The Make feature is the brand name of the Car.
* `Model` : The Model feature is the brand of model or different version of Car models.
* `Year` : The year describes the year of launched.
* `Engine Fuel Type` : It defines the Fuel type of the car model.
* `Engine HP` : Engine HP means Horsepower that refers to the power an engine produces.
* `Engine Cylinders` : Engine Cylinders are number of cylinders in present in the engine.
* `Transmission Type` : It is the type of feature that describe about the car transmission type i.e Mannual or automatic.
* `Driven_Wheels` : The type of wheel drive.
* `No of doors` : It defined number of doors present in the car.
* `Market Category` : This features tells about the type of car or which category the car belongs.
* `Vehicle Size` : It's say about the about car size.
* `Vehicle Style` : The feature is all about the style that belongs to car.
* `highway MPG` : The average a car will get while driving on an open stretch of road without stopping or starting, typically at a higher speed.
* `city mpg` : City MPG refers to driving with occasional stopping and braking.
* `Popularity` : It can refered to rating of that car or popularity of car.

Target variable:
* `MSRP` : The price of that car.

Dataset Source Link :
https://github.com/paragj30/car_price_prediction_end_to_end/blob/main/notebook/data/Cars_data.csv


### Approach for the project 

1. Data Ingestion : 
    * In Data Ingestion phase the data is first read as csv. 
    * Then the data is split into training and testing and saved as csv file.

2. Data Transformation : 
    * In this phase a ColumnTransformer Pipeline is created.
    * for Numerical Variables first SimpleImputer is applied with strategy median , then Standard Scaling is performed on numeric data.
    * for Categorical Variables SimpleImputer is applied with most frequent strategy, then ordinal encoding performed , after this data is scaled with Standard Scaler.
    * Performed dimensionality reduction techinque using TruncatedSVD method on categorical and numerical Variables. 
    * This preprocessor is saved as pickle file.

3. Model Training : 
    * In this phase base model is tested. The best model found was DecisionTreeRegressor.
    * After this hyperparameter tuning is performed on DecisionTreeRegressor and multiple model to get the best training r2 score.
    * A final DecisionTreeRegressor is selected.
    * This model is saved as pickle file.

4. Prediction Pipeline : 
    * This pipeline converts given data into dataframe and has various functions to load pickle files and predict the final results in python.

5. Flask App creation : 
    * Flask app is created with User Interface to predict the gemstone prices inside a Web Application.

# Exploratory Data Analysis Notebook

Link : [EDA Notebook](./notebook/EDA_car_price_prediction.ipynb)

# Model Training Approach Notebook

Link : [Model Training Notebook](./notebook/model_training.ipynb)