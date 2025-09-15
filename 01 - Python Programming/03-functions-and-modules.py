# Function with parameters and return value
def add_number(number1, number2):
    return number1 + number2

result = add_number(1, 2)
print("Sum: ", result)

# Local Scope
def greet():
    message = "Hello, world!"
    print(message)

greet()

# Global Scope
greeting = "Hi"

def say_hello():
    print(greeting)

say_hello()
greet()

# Modules
import math             # import an entire module
print(math.sqrt(5))

from math import sqrt   # import specific functions
print(sqrt(5))

import math as m        # use aliases
print(m.sqrt(5))