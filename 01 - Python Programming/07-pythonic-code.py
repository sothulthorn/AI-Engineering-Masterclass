"""
Best Practices
- Use descriptive variable names
- Write modular code with functions and classes
- Follow PEP 8 style guidelines
- Avoid redundancy; leverage Python's powerful built-ins
"""
#######################
# List Comprehensions
# - A concise way to create lists using a single line of code
# [expression for item in iterable if condition]
#######################
# Create a list of squares
squares = [x**2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Filter Even Numbers
evens = [x for x in range(10) if x % 2 == 0]
print(evens) # [0, 2, 4, 6, 8]

#######################
# Lambda Functions
# - Anonymous, single-expression functions defined using the lambda keyword
# lambda agruments: express
#######################
add = lambda x, y: x + y
print(add(3, 5))

"""
Common function
- map() - Applies a function to each item in a iterable
- filter() - Filters items based on a condition
- reduce() - Reduces an iterable to a single value
"""
# .map()
numbers = [1, 2, 3, 4]
squares = map(lambda x: x**2, numbers)
print(list(squares))  # [1, 4, 9, 16]

# .filter()
evensList = filter(lambda x: x % 2 == 0, numbers)
print(list(evensList)) # [2, 4]

# .reduce()
from functools import reduce
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # 24

"""
Python's os and sys modules
os Module
- Provides functions to interact with the operating system
sys Module
- Provide access to system-specific parameters and functions
"""
# os module
import os
print(os.getcwd())
os.mkdir('testdir')

# sys module
import sys
print(sys.argv)
print(sys.version)