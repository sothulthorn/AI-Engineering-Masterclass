# if-else
# Example 1: Checking a condition
num = 10
if num > 0:
    print("Positive Number")
elif num == 0:
    print("Zero")
else:
    print("Negative Number")

# Example 2: Nested Conditions
age = 25
if age > 18:
    if age < 30:
        print("Young Adult")
    else:
        print("Adult")

# for-loop
# Loop through a list of item
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Loop with range
for i in range(5):
    print(i)

# while-loop
# Count down from 5
count = 5
while count > 0:
    print(count)
    count -= 1

# break and continue
# break -> terminates the loop prematurely when a condition is met
for i in range(10):
    if i == 7:
        break
    print(i)

# continue -> skips the current iteration and proceeds to the next
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)