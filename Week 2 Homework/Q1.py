# 1) From df filter the 'Manufacturer', 'Model' and 'Type' for every 20th row starting from 1st (row 0).
# df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

import pandas as pd

# Loaded the DataFrame 'df' from the given URL
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

# Filter the 'Manufacturer', 'Model' and 'Type' for every 20th row starting from 1st (row 0)
result = df.iloc[::20, [0, 1, 2]]
result.columns = ['Manufacturer', 'Model', 'Type']

print(result)