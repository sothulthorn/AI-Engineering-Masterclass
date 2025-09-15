##############
# Lists
############## 
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

##############
# Tuples
##############
colors = ("red", "green", "blue")
single_item = ("glass",)

# Access Element
print(colors[0])
print(colors[-1])

##############
# Dictionary
##############
student = {"name": "John", "age": 25, "grade": "A"}
print(student)

# Access Element
print(student["name"])
print(student["age"])
print(student["grade"])

# Add or Update
student["subject"] = "Python"   # add
student["age"] = 28 # update

# Remove
del student["grade"]
student.pop("grade")
print(student)

# Iteration
for key, value in student.items():
    print(key, value)

##############
# Sets
##############
numbers = {1, 2, 3}
empty_set = set()

# Adding and Remove element
numbers.add(4)
numbers.remove(3)

# Set Operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 | set2)  # union
print(set1 & set2)  # intersection
print(set1 - set2)  # difference

