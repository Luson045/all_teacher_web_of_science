import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.metrics import mean_squared_error
import numpy as np

numerical_columns = ['Total Publications', 'Total Citations', 'H-index', 'I10-index',
                     'Years in NIT J', 'Experience', 'Category Count', 'CPI ', 'CPY']

df[numerical_columns] = df[numerical_columns].apply(pd.to_numeric, errors='coerce')

num_df = df[numerical_columns]

train_data = num_df[num_df['I10-index'].notna()]
predict_data = num_df[num_df['I10-index'].isna()]

X_train = train_data.drop(columns=['I10-index'])
y_train = train_data['I10-index']

X_train_split, X_val_split, y_train_split, y_val_split = train_test_split(X_train, y_train, test_size=0.2, random_state=42)

model = xgb.XGBRegressor(objective='reg:squarederror', n_estimators=100, learning_rate=0.1)

param_dist = {
    'max_depth': np.arange(3, 16, 1),
    'learning_rate': [0.01, 0.05, 0.1, 0.2, 0.3],
    'n_estimators': np.arange(50, 301, 10),
    'subsample': [0.7, 0.8, 0.9, 1.0],
    'colsample_bytree': [0.7, 0.8, 1.0],
    'gamma': [0, 0.05, 0.1, 0.2, 0.3],
    'min_child_weight': [1, 3, 5, 7],
    'scale_pos_weight': [1, 2, 3]
}

random_search = RandomizedSearchCV(
    estimator=model,
    param_distributions=param_dist,
    n_iter=100,
    cv=5,
    scoring='neg_mean_squared_error',
    verbose=2,
    n_jobs=-1,
    random_state=42
)

random_search.fit(X_train_split, y_train_split)

best_params = random_search.best_params_
print(f"Best Parameters from Randomized Search: {best_params}")

best_model = random_search.best_estimator_

y_val_pred = best_model.predict(X_val_split)

mse_val = mean_squared_error(y_val_split, y_val_pred)
print(f"Validation Mean Squared Error: {mse_val:.4f}")

X_predict = predict_data.drop(columns=['I10-index'])
predicted_I10 = best_model.predict(X_predict)

df.loc[df['I10-index'].isna(), 'I10-index'] = predicted_I10

print("\nDataFrame with Filled Missing I10-index Values:")
print(df.head())

y_full_pred = best_model.predict(X_train)
mse_full = mean_squared_error(y_train, y_full_pred)
print(f"\nTraining Set Mean Squared Error: {mse_full:.4f}")
