import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

#load data
df = pd.read_csv("k_means_cluster_model_dataset.csv")
# print(df.head())

#Features selected for clustering
X = df[
    [
        'Age',
        'Annual_Income',
        'Spending_Score',
        'Monthly_Store_Visits',
        'Online_Engagement_Score'
    ]
]
print(f"X : {X}")

#Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

#elbow method to determine optimal number of clusters
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i,
                     init='k-means++', 
                     random_state=42)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

#plotting the elbow method
plt.plot(range(1, 11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()

#final model with K means
kmeans = KMeans(n_clusters=5, 
                init='k-means++', 
                random_state = 42
)

y_kmeans = kmeans.fit_predict(X_scaled)
print(f"y_kmeans : {y_kmeans}")

# #PCA for visualization  
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# #plotting the clusters
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y_kmeans, cmap='viridis')
plt.title('K-Means Clustering (PCA Visualization)')
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')
plt.show()

# #cluster centers
centers = scaler.inverse_transform(kmeans.cluster_centers_)
print(f"Cluster Centers (original scale):\n{centers}")
print(f"Cluster Centers (scaled):\n{kmeans.cluster_centers_}")

# #cluster suummary
cluster_summary = pd.DataFrame(centers, columns=X.columns)
print(f"Cluster Summary:\n{cluster_summary}")

print("K-Means clustering completed successfully.")

