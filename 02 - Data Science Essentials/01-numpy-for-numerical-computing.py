"""
Why use Numpy in AI?
- Performance
- Ease of Use
- Integration
"""
import numpy as np

# Create array
arr = np.array([1, 2, 3, 4])
print(arr)  # [1, 2, 3, 4]

# Using built-in function
zeroes = np.zeros((3, 3))
print(zeroes) # [[0. 0. 0.] [0. 0. 0.] [0. 0. 0.]]

ones = np.ones((2, 4))
print(ones) # [[1. 1. 1. 1.] [1. 1. 1. 1.]]

range_arr = np.arange(1, 10, 2)
print(range_arr) # [1 3 5 7 9]

linspace = np.linspace(0, 1, 5)
print(linspace) # [0. 0.25 0.5 0.75 1.0]

# Manipulating Arrays
# reshape
arr = np.array([1, 2, 3, 4, 5, 6])
reshaped = arr.reshape(2, 3)
print(reshaped) # [[1 2 3][4 5 6]]

# Adding dimension
arr = np.array([1, 2, 3])
expanded = arr[:, np.newaxis]
print(expanded) # [[1][2][3]]

# Basic Operations on Arrays
# Element-wise
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a + b) # [5 7 9]
print(a * b) # [4 10 18]
print(a / b) # [0.25 0.4 0.5]

# Mathematical
arr = np.array([4, 16, 25])
print(np.sqrt(arr)) # [2. 4. 5.]
print(np.sum(arr))  # 45
print(np.mean(arr)) # 15.0
print(np.max(arr))  # 25

# Array Indexing, Slicing and Reshaping
# Indexing
arr = np.array([10, 20, 30, 40, 50, 60])
print(arr[2])   # 30
print(arr[-1])  # 50

# Slicing
print(arr[1:4]) # [20 30 40]
print(arr[:3])  # [10 20 30]
print(arr[3:])  # [40 50, 60]

# Reshaping
reshaped = arr.reshape(2, 3)
print(reshaped) # [[10 20 30][40 50 60]]