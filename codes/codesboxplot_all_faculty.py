import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

palette = {'AP1': '#35697d', 'AP2': '#df7a55', 'AP': '#56de7a', 'P': '#964c7d'}

fig, ax = plt.subplots(figsize = (12, 6))
sns.boxplot(x = 'h_index', y = 'grade', data = df, ax = ax, palette = palette)

ax.set_yticklabels(['Assistant Professors (Grade - 1)'
                    , 'Assistant Professors (Grade - 2)'
                    , 'Associate Professors', 'Professors']
                   , color = 'k')

ax.set_title('H Indices of all Faculty Members', fontweight = 'bold', fontsize = 15)
ax.set_xlabel('H Indices', fontsize = 12)
ax.set_ylabel('Designation', fontsize = 15)
ax.set_xticks([i for i in range(2, 23, 4)])
plt.tight_layout()

plt.show()
