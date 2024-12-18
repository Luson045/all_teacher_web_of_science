from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters = 2, random_state = 42)
df['Cluster'] = kmeans.fit_predict(umap_embeddings)


plt.scatter(umap_embeddings[:, 0], umap_embeddings[:, 1], c = df['Cluster'], cmap = 'rainbow', alpha = 0.9)
plt.title('UMAP with K-means Clustering')
plt.xlabel('UMAP Component 1')
plt.ylabel('UMAP Component 2')
plt.colorbar(label = 'Cluster')
plt.savefig('/Users/harshvirmangla/Downloads/UMAPClusters.png', dpi = 500, bbox_inches = 'tight')
plt.show()
