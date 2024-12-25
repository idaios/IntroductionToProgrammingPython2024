import numpy as np
import pandas as pd

fname = '/home/motoo/teaching/2024_2025/python/lecture9/GDS4891.clean'

a = pd.read_csv(fname, delimiter='\t', header=0, na_values="null")

data = a.iloc[:,2:]
genenames = a.iloc[:,1]

# kanonikopoiisi
mydata = (data - data.mean(axis=0, skipna=True))/data.std(axis=0, skipna=True)
cleanmydata = mydata.dropna()




## let's create a simple statistic to get differential expression genes
## 8 - 20 is group1

class1_data = cleanmydata.iloc[:,7:20]
class2_data = cleanmydata.iloc[:,20:]

import time
stime = time.time()


from scipy import stats
tstat = []
pvalues = []
goodIndices = []
'''
for i in range(cleanmydata.shape[0]):
    geneclass1 = class1_data.iloc[i]
    geneclass2 = class2_data.iloc[i]
    ttest, pval = stats.ttest_ind(geneclass1, geneclass2, equal_var = False)
    tstat.append(ttest)
    pvalues.append(pval)
etime = time.time()

print(f"first timing is {etime-stime}")
'''

import numpy as np
from scipy import stats

stime = time.time()
# Convert to numpy arrays for faster element-wise operations
class1_data = class1_data.to_numpy()
class2_data = class2_data.to_numpy()

# Perform t-test for all genes (assuming both class1_data and class2_data have shape (n_genes, n_samples))
tstat, pvalues = stats.ttest_ind(class1_data, class2_data, axis=1, equal_var=False)

filteredGenes = genenames[cleanmydata.index]

print(f"second time is {time.time() - stime}")




# correct for multiple testing
from statsmodels.stats.multitest import multipletests
corrected_pvalues = multipletests(pvalues, alpha=0.05, method='fdr_bh')[1]



pvalues

dfpval = pd.DataFrame({"Uncorrected":pvalues, 
                       "FDR": corrected_pvalues})

sorteddf = dfpval.sort_values(by="FDR")
print(sorteddf)


dfpval['FDR'] < 0.05
filteredGenes

#filteredGenes[dfpval['FDR'] < 0.05]

importGenes = filteredGenes[dfpval['FDR'] < 0.05]

importdf = pd.DataFrame({'gene': importGenes,
                         'fdr': dfpval[dfpval['FDR'] < 0.05]['FDR'],
                         'pval': dfpval[dfpval['FDR'] < 0.05]['Uncorrected']})

print(importdf)

importdf.to_csv('importantGenes.csv')