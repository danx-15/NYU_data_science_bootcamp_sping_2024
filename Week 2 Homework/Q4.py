# 4)Create a 4x4 NumPy array filled with random integers between 1 and 100. 
# Then, reshape this array into two separate 2D arrays, where one represents the rows and the other represents the columns. 
# Write a function, preferably using a lambda function, to calculate the sum of each row and each column separately, 
# and return the results as two separate NumPy arrays

import numpy as np

# Create a 4x4 NumPy array filled with random integers between 1 and 100
arr = np.random.randint(1, 101, size=(4, 4))

# Reshape the array into two separate 2D arrays representing rows and columns
rows = arr.reshape(4, 4)
cols = arr.reshape(4, 4)

# Calculate the sum of each row and each column separately using lambda functions
row_sums = np.apply_along_axis(lambda x: np.sum(x), axis=1, arr=rows)
col_sums = np.apply_along_axis(lambda x: np.sum(x), axis=0, arr=cols)

# Return the results as two separate NumPy arrays
row_sums_array = np.array(row_sums)
col_sums_array = np.array(col_sums)

row_sums_array, col_sums_array

print("Original array:")
print(arr)
print("\nRow sums:")
print(row_sums_array)
print("\nColumn sums:")
print(col_sums_array)