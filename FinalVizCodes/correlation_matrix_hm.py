import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

numerical_columns = ['Total Publications', 'Total Citations', 'H-index', 'I10-index', 
                     'Years in NIT J', 'Experience', 'Category Count', 'CPI ', 'CPY']

correlation_matrix = df[numerical_columns].corr()
np.fill_diagonal(correlation_matrix.values, 0)
mask = np.triu(np.ones_like(correlation_matrix, dtype = bool))

plt.figure(figsize = (18, 15))
sns.heatmap(correlation_matrix, annot = True, fmt = ".3f", cmap = "inferno_r", cbar = True, mask = mask)
plt.title("Correlations of Research Metrics", weight = 'bold', fontsize = 20)
plt.yticks(rotation = 0)
# print(correlation_matrix)
plt.savefig('/Users/harshvirmangla/Downloads/co_or.png', dpi = 400, bbox_inches = 'tight')
plt.show()
