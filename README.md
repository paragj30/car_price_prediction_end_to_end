# End to end Car Price Prediction Data Science Project - Parag Jadhav 

### Introduction About the Data :

**The dataset** The goal is to predict `MSRP` of given vehicle (Regression Analysis).

There are 15 independent variables:

* `Make` : The Make feature is the brand name of the Car. e..g, 'BMW', 'Audi', 'Mercedes-Benz', 'Volvo', 'Mitsubishi', 'Ferrari', 'Porsche', 'Ford' 'Kia', 'Lamborghini', 'Rolls-Royce', ''Land Rover', 'Tesla', 'Bugatti', etc.
* `Model` : The Model feature is the brand of model or different version of Car models.
* `Year` : The year describes the year of launched.
* `Engine Fuel Type` : It defines the Fuel type of the car model. e.g., 'premium unleaded', 'regular unleaded', 'flex-fuel', 'diesel', 'electric' 'natural gas', etc.
* `Engine HP` : Engine HP means Horsepower that refers to the power an engine produces.
* `Engine Cylinders` : Engine Cylinders are number of cylinders in present in the engine.
* `Transmission Type` : It is the type of feature that describe about the car transmission type i.e Mannual or automatic. e.g., 'MANUAL', 'AUTOMATIC', 'AUTOMATED_MANUAL'.
* `Driven_Wheels` : The type of wheel drive. e.g., 'rear wheel drive', 'front wheel drive', 'all wheel drive', 'four wheel drive', etc.
* `No of doors` : It defined number of doors present in the car.
* `Market Category` : This features tells about the type of car or which category the car belongs. e.g., 'Luxury', 'Performance', 'Crossover', 'Hatchback', etc.
* `Vehicle Size` : It's say about the about car size. e.g., 'Compact', 'Midsize', 'Large'.
* `Vehicle Style` : The feature is all about the style that belongs to car. e.g., 'Coupe', 'Sedan', 'Wagon', 'Hatchback', 'SUV', 'Passenger Minivan', 'Passenger Van', etc.
* `highway MPG` : The average a car will get while driving on an open stretch of road without stopping or starting, typically at a higher speed.
* `city mpg` : City MPG refers to driving with occasional stopping and braking.
* `Popularity` : It can refered to rating of that car or popularity of car.

Target variable:
* `MSRP` : The price of that car.

Dataset Link :
[Dataset Link](https://www.kaggle.com/datasets/CooperUnion/cardataset)


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


## How to run?

### Option 1:
#### STEPS:

1. Create a virtual environment for this application.
```bash
conda create -p venv python=3.10 -y
```

2. Activate the virtual environment.
```bash
conda activate venv/
```

3. Clone this GitHub Repository.
```bash
git clone https://github.com/paragj30/car_price_prediction_end_to_end.git
```

4. Enter inside the car_price_prediction folder.
```bash
cd \folder_location
```

4. Install all the libraries and dependencies present in the "requirements.txt" file.
```bash
pip install -r "requirements.txt"
```

5. Run the application.
```bash
python app.py
```

6. Open the web browser and copy past the link below:
```bash
127.0.0.1:8080
```


### Option 2:
#### STEPS:

1. Open the Docker Desktop

2. Download the docker image:
```bash
docker pull paragj30/car_price_prediction_apps:latest
```

3. Run the docker image command:
```bash
docker run -d -p 8080:8080 paragj30/car_price_prediction_apps
```

4. Open the web browser and copy past the link below:
```bash
127.0.0.1:8080
```


## Description: About the deployment

1. Build docker image of the source code

2. Push your docker image to Elastic Container Registry (ECR) 

3. Launch Your EC2 Instance

4. Pull the image from ECR in EC2 Instance

5. Lauch your docker image in EC2 Instance


## AWS-CICD-Deployment-with-Github-Actions

### 0. Create the Dockerfile and CICD.yaml file

### 1. Login to AWS console.

### 2. Create IAM user for deployment

Policy for Identity Access Management (IAM) User with specific access:

    1. AmazonEC2ContainerRegistryFullAccess
ECR Access: Elastic Container registry to save your docker image in AWS.

    2. AmazonEC2FullAccess
EC2 access : It is virtual machine.


### 2. Create and download the Access key and Secret access key to authenticate the GitHub Action with AWS account.

    1. AWS_ACCESS_KEY_ID

    2. AWS_SECRET_ACCESS_KEY


### 3. Create ECR repository to store/save docker image

1. AWS_ECR_LOGIN_URI: Save the URI of our docker repository. This repository will be accessible to GitHub Action through this URI.

2. ECR_REPOSITORY_NAME: Save the name of the docker repository.



### 4. Create EC2 Virtual Machine (Ubuntu) 

1. Select the "Ubuntu" OS Image as it is a lightweight virtual machine compared to the Windows VM.

2. Select the Ubuntu Server LTS (free tier) with 64-bit architecture. 

3. Select the Instance Type (Configurations of the Ubuntu VM Server) RAM, CPU and memory

4. Generate the Key pair (.pem file) to securly connect to the EC2 Instance via PuttyGen/Mobaxtrem.

5. Create a Security group by selecting the SSH, HTTP and HTTPS traffic from the internet. This group is a firewall that controls the traffic of the EC2 Instance.

    5.1 Edit the Indbound rules to  run the application. Select the "Custom TCP" and add the port number (8080).

6. Launch the EC2 Instance.

7. Connect to EC2 Instance using EC2 Instance Connect(launch terminal on tab) or SSH Client(3rd party client like PuttyGen/Mobaxtrem).
 
 

### 5. Open EC2 and Install docker in EC2 Machine:

check if any external packages are installed or not

    ls 

    clear 
To update the all package manager and dependencies in VM Instane

	sudo apt-get update -y 

	sudo apt-get upgrade 

    clear
	
** Required

To check if docker is installed or not

    docker --version 

To download the docker in the EC2 virtual machine instance

	curl -fsSL https://get.docker.com -o get-docker.sh 

To check if docker.sh file is downloaded or not. docker.sh file will have all the links and command for the docker download and installtion.

    ls 

To open and read the docker.sh file.

    cat get-docker.sh 

To run the docker.sh file. This will trigger the installation of docker.

	sudo sh get-docker.sh 

	sudo usermod -aG docker ubuntu

	newgrp docker
	
    docker --version 

To check the docker images

    docker ps  



### 6. Configure EC2 as self-hosted runner:

1. Self-hosted runner is a another VM Instance present on GitHub. So we will make a EC2 Instance as Self-hosted runner, that will make a connection with GitHub to pull the updated changes from GitHub to EC2 Instance.

    
2. github_project>Setting>Actions>Runner>New self-hosted runner> choose os> then copy, paste and run command one by one on 'EC2 Instance Connect Terminal' to make the connection with GitHub.

    
    2.1 Enter the name of runner: self-hosted
    
3. Make sure that the status of the 'self-hosted' runner is always "Idle": GitHub is connected to the EC2 Instance.



### 7. Setup github secrets:

So that GitHub can access the EC2 Instance.

github_project>Setting>Actions>Secrets and variables > Actions > New repository secret > Add the below informations:
 
    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = paste the URI of the Docker repository present inside the ECR.

    ECR_REPOSITORY_NAME = simple-app



### 8. Setup .github/workflows directory inside the GitHub repository:

1. By default GitHub Actions will search the '.github/workflows' directory.

2. Create the CICD.yaml and define workflow in that file.


### 9. Open the Public URL of the Application

1. Open EC2 Instance and copy the Pubic IPv4 address and paste it in the browser URL:8080

2. Successfully deployed the application.


### 10. Change the URL.

- Buy the desried domain and change the URL to the new domain.