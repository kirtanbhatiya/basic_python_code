import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

import matplotlib.pyplot as plt   

# Load the dataset
data = pd.read_csv('multiple_linear_regrassion_model.csv')
# print(data)
print(data.head())

# Feature selection 
X = data[['house_size_sqft','bedrooms','house_age_years']] # Independent variables
# print(X.head()) # Output = fist 5 data of X
Y = data[['house_price_lakh']] #Depandent variable
# print(Y.head()) #Output = first 5 data of Y 

#train and test split data kitna data train mai jayega or kitna data test mai jayega
X_train, X_test, Y_train, Y_test =train_test_split(   
    X,
    Y,
    test_size=0.2,
    random_state=42)

#model train
model = LinearRegression()
model.fit(X_train, Y_train) 

#model prediction
Y_pred = model.predict(X_test)  
# print(Y_pred)

#model evaluation calculate mean squared error and r2 score
mse = mean_squared_error(Y_test, Y_pred)
r2 = r2_score(Y_test, Y_pred)
print(f'Mean Squared Error: {mse}')
print(f'R^2 Score: {r2}')

#new data prediction
new_data = np.array([[2000, 3, 10]]) # Example: 2000 sqft, 3 bedrooms, 10 years old
new_price_pred = model.predict(new_data)
print(f'Predicted price for the new data: {new_price_pred[0][0]:.2f} lakh')

#matplotlib visualization

plt.scatter(Y_test, Y_pred)
plt.xlabel('Actual Prices (lakh)')
plt.ylabel('Predicted Prices (lakh)')
plt.title('Actual vs Predicted House Prices')
plt.show()