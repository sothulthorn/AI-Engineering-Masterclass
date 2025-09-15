# Read File
with open("sample.txt", "r") as file:
    content = file.readlines()
    print(content)

# Write File
with open("sample.txt", "w") as file:
    file.write("Hello World")
    file.writelines(["Alice", "Bob", "Cherry"])

"""
'with' statement for file management

What is the 'with' statement?
- Ensures files are properly closed after operations, even if an exception occurs

Advantages
- Simplifies code
- Reduces the risk of file corruption

Why use Exception Handling?
- Prevents the program from crashing due to file-related errors (e.g. file not found)

Using try-except Blocks
Common File Handling Exceptions
- FileNotFoundError
- PermissionError
- IOError
"""

try:
    with open("sample.txt", "r") as file:
        content = file.readlines()
except FileNotFoundError:
    print("File not found")