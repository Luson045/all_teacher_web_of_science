import pandas as pd
import shap
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X = df.drop(columns = ['H-index', 'Professor Name', 'Professor Name.1'])
y = df['H-index'] 

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size = 0.2, random_state = 42)

model = RandomForestRegressor(n_estimators = 100, random_state = 42)
model.fit(X_train, y_train)

explainer = shap.Explainer(model, X_train)
shap_values = explainer(X_test)

shap.summary_plot(shap_values, X_test, feature_names = X.columns)

shap.waterfall_plot(shap.Explanation(values = shap_values[0].values, 
                                     base_values = shap_values[0].base_values, 
                                     data = X_test[0], 
                                     feature_names = X.columns))


import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style = "whitegrid")

plt.figure(figsize = (12, 8))

sns.barplot(
    y = importance_df['Feature'][:10],
    x = importance_df['Importance'][:10],
    palette = "Blues_d",
    orient = 'h'
)

plt.xlabel("Mean Absolute SHAP Value", fontsize = 14)
plt.ylabel("Features", fontsize = 14)
plt.title("Top 10 Metrics Influencing H-index", fontsize = 18, weight = 'bold')

plt.gca().invert_yaxis()

plt.grid(True, axis = 'x', linestyle = '--', alpha = 0.7)

plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)

plt.tight_layout()
plt.savefig('/Users/harshvirmangla/Downloads/shap.png', dpi = 300, bbox_inches = 'tight')
plt.show()
