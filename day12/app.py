# İmport Library Begin

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error , r2_score
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler , OneHotEncoder
import streamlit as st

# İmport Library End

df = pd.read_excel("cars.xls")
x = df.drop('Price' , axis= 1)
y = df[['Price']]

# Train Test Split
x_train , x_test , y_train , y_test = train_test_split(x,y ,random_state= 42 , test_size=0.2)

# Preprocessing Ön işleme

preprocessor =  ColumnTransformer(
    transformers= [
        ("num",StandardScaler(),["Mileage","Cylinder","Liter","Doors"]),
        ("cat",OneHotEncoder(),["Make","Model","Trim","Type"])
    ]
)

# Model Tanımlama
model = LinearRegression()

# Pipeline
Pipeline = Pipeline(steps=[("preprocessor", preprocessor),("regressor",model)])



