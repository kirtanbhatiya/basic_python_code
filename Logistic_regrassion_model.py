import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import  accuracy_score, precision_score, recall_score, f1_score

import matplotlib.pyplot as plt

#load the dataset
data = pd.read_csv('Logistic_regrassion_model_dataset.csv')
# print(data.head())

#feature selection
X = data[['age', 'annual_income', 'credit_score', 'loan_amount', 'employment_years', 'debt_to_income_ratio']] # Independent variables  
# print(X.head()) # Output = first 5 data of X      
Y = data['loan_default'] # Dependent variable
# print(Y.head()) # Output = first 5 data of Y

#train and test split
X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42)

#model train
model = LogisticRegression()
model.fit(X_train, Y_train)
# print(model)

#model prediction
Y_pred = model.predict(X_test)  
# print(Y_pred)

#model evaluation
print("Accuracy:", accuracy_score(Y_test, Y_pred))
print("Precision:", precision_score(Y_test, Y_pred))
print("Recall:", recall_score(Y_test, Y_pred))
print("F1 Score:", f1_score(Y_test, Y_pred))

#new data prediction
# new_data = np.array([[30, 50000, 700, 10000, 5, 0.3]]) # Example new data point
# # print(new_data) 
# new_prediction = model.predict(new_data)
# print(f'Predicted class for the newdata: {"Loan Default" if new_prediction[0] == 1 else "No Loan Default"}')

#matplotlib visualization

# plt.scatter(Y_test, Y_pred)
# plt.xlabel('Actual Values (Loan Default)')
# plt.ylabel('Predicted Values (Loan Default)')
# plt.title('Loan Default Prediction Distribution')
# plt.show()