import pandas as pd
import scipy.stats as stats

discipline_columns = [
    'Networking', 'OS', 'Optics', 'Optimization', 'Research and Experimental Medicine', 
    'Science and Technology', 'Security', 'Software Engineering', 'Telecommunication', 'Transportion'
]

citation_results = {}
h_index_results = {}

for column in discipline_columns:
    group_with_discipline = df[df[column] == 1]['Total Citations']
    group_without_discipline = df[df[column] == 0]['Total Citations']
    
    t_stat_citations, p_value_citations = stats.ttest_ind(group_with_discipline, group_without_discipline, nan_policy='omit')
    citation_results[column] = (t_stat_citations, p_value_citations)

    group_with_discipline_h = df[df[column] == 1]['H-index']
    group_without_discipline_h = df[df[column] == 0]['H-index']
    
    t_stat_h_index, p_value_h_index = stats.ttest_ind(group_with_discipline_h, group_without_discipline_h, nan_policy='omit')
    h_index_results[column] = (t_stat_h_index, p_value_h_index)

print("T-test Results for Total Citations by Discipline:")
for column, result in citation_results.items():
    print(f"{column}: T-statistic = {result[0]:.4f}, P-value = {result[1]:.4f}")

print("\nT-test Results for H-index by Discipline:")
for column, result in h_index_results.items():
    print(f"{column}: T-statistic = {result[0]:.4f}, P-value = {result[1]:.4f}")
