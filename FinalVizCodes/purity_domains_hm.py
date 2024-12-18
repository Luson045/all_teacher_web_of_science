import pandas as pd

print(df.columns)
discipline_columns = [
    'CS', 'DS', 'AI', 'Mathematics', 'Hardware', 'Mechanics', 'IT', 'IoT', 'Acoustics',
    'Networking', 'OS', 'Optics', 'Optimization', 'Research and Experimental Medicine', 
    'Science and Technology', 'Security', 'Software Engineering', 'Telecommunication', 'Transportion'
]

df_domains = df[discipline_columns]

purity_matrix = pd.DataFrame(0, index=discipline_columns, columns=discipline_columns)

for col1 in discipline_columns:
    count_col1 = (df_domains[col1] == 1).sum()
    
    for col2 in discipline_columns:
        if col1 != col2:
            count_col1_and_col2 = ((df_domains[col1] == 1) & (df_domains[col2] == 1)).sum()
            purity_matrix.loc[col1, col2] = (count_col1_and_col2 / count_col1) * 100 if count_col1 > 0 else 0

# print(purity_matrix)

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize = (20, 17))
sns.heatmap(purity_matrix, annot = True, cmap = "inferno", fmt = ".2f", cbar = True)
plt.title('Purity Matrix of Domain Co-occurrence', weight = 'bold', fontsize = 20)
plt.savefig('/Users/harshvirmangla/Downloads/purit_analysis', dpi = 1000, bbox_inches = 'tight')
plt.show()
