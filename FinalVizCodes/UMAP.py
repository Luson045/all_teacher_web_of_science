import pandas as pd
import umap
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

new_df = df.drop('Professor Name', axis = 1)
new_df.fillna(0, inplace = True)
numeric_columns = new_df.select_dtypes(include = ['float64', 'int64']).columns


scaler = StandardScaler()
scaled_data_new = scaler.fit_transform(new_df[numeric_columns])

umap_model = umap.UMAP(n_neighbors = 4, n_components = 2, random_state = 42)
umap_embeddings = umap_model.fit_transform(scaled_data_new)

tsne_model = TSNE(n_components=2, random_state = 42, perplexity = 2)
tsne_embeddings = tsne_model.fit_transform(scaled_data_new)


fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (14, 7))

# Plot UMAP results
ax1.scatter(umap_embeddings[:, 0], umap_embeddings[:, 1], c = 'blue', label = 'UMAP', alpha = 0.6)
ax1.set_title('UMAP Projection')
ax1.set_xlabel('UMAP Component 1')
ax1.set_ylabel('UMAP Component 2')

ax2.scatter(tsne_embeddings[:, 0], tsne_embeddings[:, 1], c = 'green', label = 't-SNE', alpha = 0.6)
ax2.set_title('t-SNE Projection')
ax2.set_xlabel('t-SNE Component 1')
ax2.set_ylabel('t-SNE Component 2')

plt.tight_layout()
plt.savefig('/Users/harshvirmangla/Downloads/(UMAP)&(T-SNE).png', dpi = 600, bbox_inches = 'tight')
plt.show()
