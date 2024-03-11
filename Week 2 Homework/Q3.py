# 3) How to get the rows of a dataframe with row sum > 100?
# df = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))

import pandas as pd
import numpy as np

# Create the dataframe
df = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))

# Get the rows with row sum > 100
result = df[df.sum(axis=1) > 100]

# Print the resulting dataframe
print(result)