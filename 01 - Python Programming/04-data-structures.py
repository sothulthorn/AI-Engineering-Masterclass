# Lists
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
fruits = ["apple", "banana", "cherry"]
mixed = ['apple', 1, True]

# Access Element
print(numbers[2])
print(fruits[-1])
print(mixed[1])

# Add Items
fruits.append("orange")
fruits.insert(1, "grape")

# Remove Item
fruits.remove("grape")
del fruits[2]
fruits.pop() # remove item from the last index

# Slicing
slice_fruits = fruits[1:3]
print(slice_fruits)