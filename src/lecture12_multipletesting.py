import numpy as np
import pandas as pd
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt

# Simulate the gene expression data
np.random.seed(42)
n_genes = 1000  # Rows representing genes
n_individuals = 40  # Columns representing individuals
mean_expression = 100
std_expression = 3

# Generate data
data = np.random.normal(loc=mean_expression, scale=std_expression, size=(n_genes, n_individuals))

# Split data into groups A and B
group_A = data[:, :20]  # First 20 columns are group A
group_B = data[:, 20:]  # Last 20 columns are group B

# Perform t-tests along axis=1
tstats, pvalues = ttest_ind(group_A, group_B, axis=1, equal_var=False)

# Convert p-values to a pandas DataFrame and sort
pvalues_df = pd.DataFrame({"Gene": np.arange(n_genes), "p-value": pvalues})
pvalues_df = pvalues_df.sort_values(by="p-value")

# Plot sorted p-values
plt.figure(figsize=(10, 6))
plt.plot(np.arange(len(pvalues_df)), pvalues_df["p-value"], marker='.', linestyle='none', alpha=0.7, color="blue")
plt.axhline(0.05, color="red", linestyle="--", label="Significance Threshold (0.05)")
plt.title("Sorted p-values from t-tests")
plt.xlabel("Gene Rank (sorted by p-value)")
plt.ylabel("p-value")
plt.legend()
plt.grid(alpha=0.3)
plt.show()


import pandas as pd

def fdr_correction_pandas(pvalues, alpha=0.05):
    """
    Perform FDR correction using the Benjamini-Hochberg procedure with pandas.

    Parameters:
    - pvalues: list or pandas Series of p-values
    - alpha: significance level for FDR correction (default: 0.05)

    Returns:
    - corrected_pvalues: pandas Series of FDR-adjusted p-values
    - significant: pandas Series of booleans indicating significant results
    """
    # Create a DataFrame to handle p-values with ranks
    df = pd.DataFrame({"pvalue": pvalues})
    df["rank"] = df["pvalue"].rank(method="min")  # Rank p-values (1-based index)
    m = len(pvalues)  # Total number of hypotheses

    # Calculate adjusted p-values
    df["adjusted_pvalue"] = (df["pvalue"] * m) / df["rank"]

    # Ensure monotonicity (adjusted p-values should not decrease)
    df = df.sort_values("rank", ascending=False)  # Sort by rank descending
    df["adjusted_pvalue"] = df["adjusted_pvalue"].cummin()  # Apply cumulative min
    df = df.sort_index()  # Return to original order

    # Determine significance
    significant = df["adjusted_pvalue"] < alpha

    return df["adjusted_pvalue"], significant
