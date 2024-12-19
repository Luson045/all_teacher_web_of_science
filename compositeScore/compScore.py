dff = df.copy()
dff[['H-index', 'Total Citations', 'Total Publications', 'Experience', 'I10-index', 'Category Count']] = df[['H-index', 'Total Citations', 'Total Publications', 'Experience', 'I10-index', 'Category Count']].apply(zscore)

dff['Composite Score'] = dff[['H-index', 'Total Citations', 'Total Publications', 'I10-index']].mean(axis = 1)
dff['Cluster Rank'] = dff.groupby('Cluster')['Composite Score'].rank(ascending = False)

threshold_high = 0.15
threshold_low = -0.56

def rank_cluster(row):
    if row['Composite Score'] >= threshold_high:
        return 'High Impact'
    elif row['Composite Score'] >= threshold_low:
        return 'Moderate Impact'
    else:
        return 'Low Impact'

dff['Cluster Label'] = dff.apply(rank_cluster, axis = 1)

import pandas as pd
import matplotlib.pyplot as plt

mean_composite_score = dff.groupby('Cluster')['Composite Score'].mean()
median_composite_score = dff.groupby('Cluster')['Composite Score'].median()
std_composite_score = dff.groupby('Cluster')['Composite Score'].std()

mean_experience = dff.groupby('Cluster')['Experience'].mean()
median_experience = dff.groupby('Cluster')['Experience'].median()
std_experience = dff.groupby('Cluster')['Experience'].std()

x_labels = mean_composite_score.index
bar_width = 0.25

fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (16, 6))

ax1.bar(x_labels - bar_width, mean_composite_score, bar_width, label = 'Mean', color = 'skyblue', edgecolor = 'black')
ax1.bar(x_labels, median_composite_score, bar_width, label = 'Median', color = 'orange', edgecolor = 'black')
ax1.bar(x_labels + bar_width, std_composite_score, bar_width, label = 'Std Dev', color = 'green', edgecolor = 'black')

ax1.set_xlabel('Cluster', fontsize = 14)
ax1.set_ylabel('Composite Score', fontsize = 14)
ax1.set_title('Composite Score Metrics Across Clusters', fontsize = 16, fontweight = 'bold')
ax1.set_xticks(x_labels)
ax1.set_xticklabels([f'Cluster {i}' for i in x_labels])
ax1.legend()

ax2.bar(x_labels - bar_width, mean_experience, bar_width, label = 'Mean', color = 'skyblue', edgecolor = 'black')
ax2.bar(x_labels, median_experience, bar_width, label = 'Median', color = 'orange', edgecolor = 'black')
ax2.bar(x_labels + bar_width, std_experience, bar_width, label = 'Std Dev', color = 'green', edgecolor = 'black')

ax2.set_xlabel('Cluster', fontsize = 14)
ax2.set_ylabel('Experience', fontsize = 14)
ax2.set_title('Experience Metrics Across Clusters', fontsize = 16, fontweight = 'bold')
ax2.set_xticks(x_labels)
ax2.set_xticklabels([f'Cluster {i}' for i in x_labels])
ax2.legend()

plt.tight_layout()
plt.show()
