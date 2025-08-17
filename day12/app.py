# İmport Library Begin

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error , r2_score
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
pipeline = Pipeline(steps=[("preprocessor", preprocessor),("regressor",model)])

# training - model eğitme

pipeline.fit(x_train, y_train)


# Predict
pred = pipeline.predict(x_test)

# Calculate scores
rmse = mean_squared_error(y_test , pred)**0.5
r2 = r2_score(y_test, pred)


# prediction function
def price_pred(make , model , trim , mileage , type_ ,cyliner, liter , doors , cruise , sound , leather ):
    input_data = pd.DataFrame({
        'Make': [make],
        'Model': [model],
        'Trim': [trim],
        'Mileage': [mileage],
        'Type': [type_],
        'Cylinder': [cyliner],
        'Liter': [liter],
        'Doors': [doors],
        'Cruise': [cruise],
        'Sound': [sound],
        'Leather': [leather]
    })
    prediction = pipeline.predict(input_data)[0]
    return prediction

st.title('MLOps Car Price Prediction App :red_car:')

st.write('Enter Car Details to Predict the Price')

# Selectbox 
make = st.selectbox('Make', df['Make'].unique())
car_model = st.selectbox('Model',df[df['Make']==make]['Model'].unique())
car_model = st.selectbox('Model',df[df['Make']==make]['Model'].unique())
