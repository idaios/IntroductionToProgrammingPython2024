import pandas as pd
# from scipy.stats import ttest_ind

# Sample DataFrame
data = pd.DataFrame({
    'A1': [5, 6, 7],
    'A2': [6, 7, 8],
    'B1': [5, 5, 6],
    'B2': [4, 5, 7]
})


x = data.iloc[0,:2]
y = data.iloc[0,2:4]
m = x.mean() - y.mean()
print(m)


print(data.shape)

ms = []
for i in range(data.shape[0]):
    x = data.iloc[i,:2]
    y = data.iloc[i,2:4]
    m = x.mean() - y.mean()
    ms.append(m)


def meandif(grp1, grp2):
    m = grp1.mean() - grp2.mean()
    return m



def meandif_df(df, i1, i2, j1, j2):
    ms = []
    for x in range(df.shape[0]):
        m = meandif(df.iloc[x, i1:(i2)], df.iloc[x, j1:(j2)])
        ms.append(m)
    return ms

print(meandif_df(data.iloc[:3,:], 0, 2, 2, 4))

'''
# Define the t-test function
def row_t_test(group1, group2):
    t_stat, p_value = ttest_ind(group1, group2)
    return pd.Series([t_stat, p_value], index=['t_statistic', 'p_value'])

results = []
for i in range(data.shape[0]):
    t,p=row_t_test(data.iloc[i,:2], data.iloc[i,2:4])
    results.append((t,p))

print(results)

# Apply the function row-wise
data[['t_statistic', 'p_value']] = data.apply(row_t_test, axis=1)

print(data)
'''