import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import  accuracy_score, precision_score, recall_score, f1_score

import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('Dt_Rf_model_dataset.csv')
# print(data.head())

#feature selection
X = data[['Age','Monthly_Income','Years_At_Company','Job_Satisfaction','Overtime','Work_Life_Balance','Distance_From_Home_km','Training_Hours_Per_Year','Promotion_Last_3_Years']]
y = data['Attrition']

#train test split
X_train, X_test, y_train, y_test = train_test_split(
    X, 
    y, 
    test_size=0.2, 
    random_state=42
)

# Decision Tree Classifier
dt = DecisionTreeClassifier(random_state=42)
dt.fit(X_train, y_train)
y_pred_dt = dt.predict(X_test)

# Random Forest Classifier
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)

# Decision Tree Evaluation Metrics
print("Decision Tree Classifier:")
print("Accuracy:", accuracy_score(y_test, y_pred_dt))
print("Precision:", precision_score(y_test, y_pred_dt))
print("Recall:", recall_score(y_test, y_pred_dt))
print("F1 Score:", f1_score(y_test, y_pred_dt))
print("\nRandom Forest Classifier:")

#Random Forest Evaluation Metrics
print("Accuracy:", accuracy_score(y_test, y_pred_rf))
print("Precision:", precision_score(y_test, y_pred_rf))
print("Recall:", recall_score(y_test, y_pred_rf))
print("F1 Score:", f1_score(y_test, y_pred_rf))

Feature Importance for Decision Tree
dt_importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": dt.feature_importances_
}).sort_values(by="Importance", ascending=False)
print("\nDecision Tree Feature Importance:")
print(dt_importance)

# Feature Importance for Random Forest
rf_importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": rf.feature_importances_
}).sort_values(by="Importance", ascending=False)
print("\nRandom Forest Feature Importance:")
print(rf_importance)

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.barh(X.columns, dt.feature_importances_)
plt.title("Decision Tree Feature")
plt.xlabel("Importance")
plt.subplot(1, 2, 2)
plt.barh(X.columns, rf.feature_importances_)
plt.title("Random Forest Feature")
plt.xlabel("Importance")
plt.tight_layout()
plt.show()