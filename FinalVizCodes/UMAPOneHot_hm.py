import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

print(df.columns)
one_hot_columns = [
    'Networking', 'DS', 'CS', 'AI', 'Mathematics', 'Hardware', 'OS', 'Optics', 'Optimization', 'Research and Experimental Medicine', 
    'Science and Technology', 'Security', 'Software Engineering', 'Telecommunication', 'Transportion',
    'Electronics', 'IT', 'IoT', 'Acoustics', 'Image Processing', 'Mechanics', 'Communication Systems',
    'Automation and Control Systems', 'Cardiovascular System and Cardiology',
    'Endocrynology and Metabolism', 'Energy and Fuels', 'Software Engineering', 'Engineering'
]

one_hot_df = df[one_hot_columns]

feature_proportions = one_hot_df.groupby(df['Cluster']).mean()

plt.figure(figsize = (4, 10))
sns.heatmap(feature_proportions.T, annot = True, cmap = 'PiYG_r', cbar = True)
plt.title('Proportion of One-Hot Encoded Features per Cluster indentified in UMAP', weight = 'bold')
plt.xlabel('One-Hot Encoded Features')
plt.ylabel('Cluster')
plt.savefig('/Users/harshvirmangla/Downloads/UMAPOneHotEncoding.png', dpi = 1000, bbox_inches = 'tight')
plt.show()
