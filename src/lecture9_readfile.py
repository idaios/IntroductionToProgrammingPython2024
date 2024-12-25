import numpy as np
    
fname = '/home/motoo/teaching/2024_2025/python/lecture9/GDS4891.clean'
    

import pandas as pd
a = pd.read_csv(fname, delimiter='\t', header=0, na_values="null")
print(a)


print(a.iloc[0,0])


data = a.iloc[:, 2:]
print(data)

columnnames = data.columns.to_list()
print(columnnames)


genenames = a.iloc[:,1].to_list()
print(genenames)

mean_values = data.mean(axis=0, skipna=True)
print(mean_values)

row_mean = data.mean(axis=1, skipna=True)
print(row_mean)

x = row_mean[0]
print(x)

mean_0 = data - data.mean(axis=0)
print(mean_0)

print(mean_0.mean())


colvar = data.var(axis=0)

## general code for substract
data2 = data.subtract(data.mean(axis=1, skipna=True), axis=0)
print(data2)
rowmeans = data2.mean(axis=1, skipna=True)
print(rowmeans.to_list())

print(data.iloc[4,:])
print(data.iloc[5,:])