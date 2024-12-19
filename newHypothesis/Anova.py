from scipy.stats import f_oneway

for feature in features:
    groups = [df[df['Cluster'] == cluster][feature] for cluster in df['Cluster'].unique()]
    f_stat, p_value = f_oneway(*groups)
    print(f'{feature}: F-stat = {f_stat}, p-value = {p_value}')

# Total Citations: F-stat = 42.71459297868056, p-value = 1.4644164097993107e-07
# H-index: F-stat = 35.46419587455979, p-value = 5.702806048501307e-07
# Total Publications: F-stat = 64.97555781165323, p-value = 5.8396705569433314e-09
# Experience: F-stat = 2.875174690467379, p-value = 0.08249403021645513
# I10-index: F-stat = 48.84446531283022, p-value = 5.3435058087720155e-08
# Category Count: F-stat = 27.391061009010432, p-value = 3.4612273227008535e-06
