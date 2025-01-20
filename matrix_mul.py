import pandas as pd
import numpy as np

# Load data
# data = pd.read_csv('path/to/data')

# Example arrays
Prices = [[300, 500],
          [1000, 120.85]]

Array2 = [200,100]

# Calculate the result
Ans = []
# (300*200 + 500*100) as an example calculation

# Set the range to 1 to multiply the first index of prices inorder to implement the example calculation
for i in range(1):
    row_sum = 0
    for j in range(len(Array2)):
        # COMPLETE THE MISSING LOGIC HERE
        row_sum += Prices[i][j] * Array2[j]
        pass

Ans.append(row_sum)
print(Ans)
