import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

melted_df = pd.melt(df, id_vars = ['Cluster'], 
                    value_vars = ['Total Citations', 'H-index', 'Total Publications', 'Experience', 'I10-index', 'Category Count'], 
                    var_name = 'Feature', value_name = 'Value')

fig, axes = plt.subplots(2, 3, figsize = (20, 14))

features = ['Total Citations', 'H-index', 'Total Publications', 'Experience', 'I10-index', 'Category Count']

axes = axes.flatten()

for i, feature in enumerate(features):
    sns.boxplot(x = 'Cluster', y = 'Value', data = melted_df[melted_df['Feature'] == feature], 
                palette = 'viridis', showfliers = False, ax = axes[i])
    axes[i].set_title(f'Boxplot of {feature}', fontsize = 16, weight = 'bold')
    axes[i].set_xlabel('Cluster', fontsize = 12)
    axes[i].set_ylabel('Value', fontsize = 12)
    axes[i].tick_params(axis = 'x', rotation = 0) 

plt.tight_layout()
plt.savefig('/Users/harshvirmangla/Downloads', dpi = 400, bbox_inches = 'tight')
plt.show()
