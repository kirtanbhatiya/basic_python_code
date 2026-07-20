import pandas as pd

import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_moons

#dataset
X, y = make_moons(
    n_samples=200, 
    noise=0.1, 
    random_state=42
)

#visualize Dataset
plt.scatter(X[:,0], X[:,1])
plt.title("Moon Dataset")
plt.show()

#Scaling data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

#Apply DBSCAN algorithm
dbscan = DBSCAN(eps=0.2, min_samples=5)
y_pred = dbscan.fit_predict(X_scaled)

#visualize DBSCAN results
plt.scatter(X_scaled[:,0], X_scaled[:,1], c=y_pred, cmap='viridis')
plt.title("DBSCAN Clustering")
plt.show()


#Experiment with changing eps values
eps_values = [0.1, 0.2, 0.3, 0.4]
for eps in eps_values:
    dbscan = DBSCAN(eps=eps, min_samples=5)
    y_pred = dbscan.fit_predict(X_scaled)

    plt.scatter(X_scaled[:,0], X_scaled[:,1], c=y_pred, cmap='viridis')
    plt.title(f"DBSCAN Clustering (eps={eps})")
    plt.show()

#Compare clustering output variations
plt.figure(figsize=(12, 8))
for i, eps in enumerate(eps_values):
    dbscan = DBSCAN(eps=eps, min_samples=5)
    y_pred = dbscan.fit_predict(X_scaled)

    plt.subplot(2, 2, i+1)
    plt.scatter(X_scaled[:,0], X_scaled[:,1], c=y_pred, cmap='viridis')
    plt.title(f"DBSCAN Clustering (eps={eps})")

    