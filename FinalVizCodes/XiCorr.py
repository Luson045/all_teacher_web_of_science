import numpy as np
from scipy.stats import rankdata, norm




def xi_correlation(x, y, continuous = False):
    """Compute the correlation coefficient between x and y according to the xi coefficient defined by Chatterjee.

    Usage::
        >>> size = 250
        >>> x = np.linspace(start=-5, stop=5, num=size)
        >>> y = x / 2 + np.sin(x) + 0.2 * np.random.normal(size)
        >>> xi_correlation(

    :param x: A list.
    :param y: A list.
    :rtype: A tuple of real.
    """
    
    
    
    def rank_order(vector):
        random_index = np.random.choice(np.arange(length), length, replace = False)
        randomized_vector = vector[random_index]
        ranked_vector = rankdata(randomized_vector, method = "ordinal")
        answer = [ranked_vector[j] for _, j in sorted(zip(random_index, range(length)))]
        return answer
    
    
    
    
    def compute_d_sequence(y):
        l = rankdata([-i for i in y], method = "max")
        return np.sum(l * (length - l)) / (length ** 3)
    
    
    
    
    def compute_xi_coefficient(vector):
        mean_absolute = np.sum(np.abs([a - b for a, b in zip(vector[:- 1], vector[1:])]))
        return 1 - mean_absolute / (2 * (length ** 2) * d_sequence)
    
    
    
    
    def compute_p_value(continuous=continuous):
        
        if continuous:
            sigma = 2 / 5
        
        else:
            sorted_x_ordered = sorted(x_ordered_max_rank)
            
            index = [i for i in range(1, length + 1)]
            doubled_index = [2 * length - 2 * i + 1 for i in index]
            cumulative_sum = np.cumsum(sorted_x_ordered)
            
            a = np.sum([i * (u ** 2) for i, u in zip(doubled_index, sorted_x_ordered)]) / (length ** 4)
            b = np.sum([v + (length - i) * u for i, u, v in zip(index, sorted_x_ordered, cumulative_sum)]) / (length ** 5)
            c = np.sum([i * u for i, u in zip(doubled_index, sorted_x_ordered)]) / (length ** 3)
            
            tau_squared = (a - 2 * b + np.square(c)) / (np.square(d_sequence))
            
            sigma = np.sqrt(tau_squared)
        
        
        
        p_value = 1 - norm.cdf(np.sqrt(length) * correlation / np.sqrt(sigma))
        
        return p_value
    
    
    
    
    
    
    
    x, y = np.array(x), np.array(y)
    length = len(x)
    
    x_ordered = np.argsort(rank_order(x))
    y_rank_max = rankdata(y, method = "max")
    x_ordered_max_rank = y_rank_max[x_ordered]
    d_sequence = compute_d_sequence(y)
    
    correlation = compute_xi_coefficient(x_ordered_max_rank)
    p_value = compute_p_value(continuous=continuous)
    
    return correlation, p_value

def xi_correlation_matrix(df, columns):
    """
    Compute the Xi correlation matrix for the specified columns in a DataFrame.

    :param df: Input pandas DataFrame.
    :param columns: List of column names to include in the correlation matrix.
    :return: DataFrame containing the Xi correlation matrix.
    """
    selected_df = df[columns].select_dtypes(include = [np.number])
    numeric_columns = selected_df.columns.tolist()
    n = len(numeric_columns)
    
    xi_matrix = pd.DataFrame(np.zeros((n, n)), index = numeric_columns, columns = numeric_columns)
    
    for i in range(n):
        for j in range(n):
            if i <= j:
                xi, _ = xi_correlation(selected_df.iloc[:, i], selected_df.iloc[:, j])
                xi_matrix.iloc[i, j] = xi
                xi_matrix.iloc[j, i] = xi
    
    return xi_matrix

columns_hm = df.columns[:10]
xi_matrix = xi_correlation_matrix(df, columns_hm)
pearson_matrix = pearson_correlation_matrix(df, columns_hm)
difference = pearson_matrix - xi_matrix
difference

plt.figure(figsize = (16, 13))
sns.heatmap(difference, annot = True, cmap = 'YlGnBu', linewidths = 0.5, fmt = ".2f", cbar = True)

plt.title("(Pearson Correlation Matrix - Xi Correlation Matrix) Heatmap", weight = 'bold')
plt.xlabel("Attributes")
plt.ylabel("Attributes")
plt.savefig('/Users/harshvirmangla/Downloads/XiCorr.png', dpi = 400, bbox_inches = 'tight')
plt.show()
