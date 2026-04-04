import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import joblib

# Load data
data = pd.read_csv('data.csv')

# Select features used in app.py
features = ['sqft_living', 'sqft_lot', 'bedrooms', 'bathrooms', 'floors', 
            'waterfront', 'view', 'condition', 'yr_built', 'yr_renovated']
X = data[features]
y = data['price']

# Initialize and fit the scaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Initialize and fit the model
model = LinearRegression()
model.fit(X_scaled, y)

# Save the model and scaler
joblib.dump(model, 'house_price_model.pkl')
joblib.dump(scaler, 'scaler.pkl')

print("Model and scaler saved successfully!")
