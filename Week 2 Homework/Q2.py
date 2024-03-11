# 2) Replace missing values in Min.Price and Max.Price columns with their respective mean (check documentation).
# df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

import pandas as pd

# Read the CSV
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

# Calculate the mean of Min.Price and Max.Price columns
min_price_mean = df['Min.Price'].mean()
max_price_mean = df['Max.Price'].mean()

# Replace missing values with mean values
df['Min.Price'].fillna(min_price_mean, inplace=True)
df['Max.Price'].fillna(max_price_mean, inplace=True)

print(df)