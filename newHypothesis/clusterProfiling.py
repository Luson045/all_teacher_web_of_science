import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

X = df[['Total Citations', 'H-index', 'Total Publications', 'Experience', 'I10-index', 'Category Count']]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

kmeans = KMeans(n_clusters = 3, random_state = 15)
df['Cluster'] = kmeans.fit_predict(X_scaled)

plt.scatter(df['Total Citations'], df['Experience'], c = df['Cluster'], cmap = 'viridis')
plt.xlabel('Total Citations')
plt.ylabel('Experience')
plt.title('K-Means Clustering of Researchers')
plt.show()

print("Cluster Centers:\n", kmeans.cluster_centers_)

cluster_profile = df.groupby('Cluster')[['Total Citations', 'H-index', 'Total Publications', 'Experience']].mean()
print(cluster_profile)

from sklearn.decomposition import PCA

pca = PCA(n_components = 2)
X_pca = pca.fit_transform(X_scaled)

plt.scatter(X_pca[:, 0], X_pca[:, 1], c = df['Cluster'], cmap = 'viridis')
plt.title('PCA of K-Means Clusters')
plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.show()

wcss = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters = k, random_state = 15)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

plt.plot(range(1, 11), wcss)
plt.title('Elbow Method (To find Optimal k)')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()

cluster_profile = df.groupby('Cluster').agg({
    'Total Citations': ['mean', 'std', 'median'],
    'H-index': ['mean', 'std', 'median'],
    'Total Publications': ['mean', 'std', 'median'],
    'Experience': ['mean', 'std', 'median'],
    'I10-index': ['mean', 'std', 'median'],
    'Category Count': ['mean', 'std', 'median']
})

print(cluster_profile)

import seaborn as sns

sns.pairplot(df, hue = 'Cluster', palette  ='viridis', vars = ['Total Citations', 'H-index', 'Total Publications', 'Experience', 'I10-index', 'Category Count'])
plt.suptitle("Pairwise Plot of Features Colored by Cluster", y = 1.02)
plt.show()
