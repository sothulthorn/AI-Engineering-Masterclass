"""
Broadcasting in NumPy
Rules of Broadcasting
- Dimensions are aligned from the right
- A dimension is compatible if:
  - It matches the other array's dimension
  - One of the dimensions is 1
"""
import numpy as np

# Array and scalar broadcasting
arr = np.array([1, 2, 3])
print(arr + 10) # [11 12 13]

matrix = np.array([[1, 2, 3], [4, 5, 6]])
vector = np.array([1, 0, 1])
print(matrix + vector) # [[2 2 4][5 5 7]]

"""
Aggregation Functions
- Aggregation functions compute summary statistics for arrays
"""
# Common Functions
arr = np.array([1, 2, 3], [4, 5, 6])
print("Sum: ", np.sum(arr))     # Sum: 21
print("Mean: ", np.mean(arr))   # Mean: 3.5
print("Max: ", np.max(arr))     # Max: 6
print("Min: ", np.min(arr))     # Min: 1
print("Standard Deviation: ", np.std(arr))          # Standard Deviation: 1.707825127659933
print("Sum along rows: ", np.sum(arr, axis=1))      # Sum along rows: [6 15]
print("Sum along columns: ", np.sum(arr, axis=0))   # Sum along columns: [5 7 9]

# Boolean Indexing and Filtering
arr = np.array([1, 2, 3, 4, 5, 6])
evens = arr[arr % 2 == 0]
print("Evens: ", evens) # [2 4 6]

arr[arr > 3] = 0
print("Modified Array: ", arr)  # [1 2 3 0 0 0]

# Random Number Generation and Setting Seeds
# Random Number Generation
random_array = np.random.rand(3, 3)
print("Random Array: ", random_array)

random_integers = np.random.randint(0, 10, size=(2, 3))
print("Random Integers: ", random_integers)

# Settings Random Seeds
np.random.seed(42)