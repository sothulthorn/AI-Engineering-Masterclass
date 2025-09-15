#########################
# String Manipulation
#########################
# Concatenation
first = "Hello"
second = "World"
result = first + " " + second
print(result)

# Slicing
text = "Python Programming"
print(text[0:6])
print(text[-11:])

# Formating
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")

# Common String Methods
# split()
sentence = "Python is fun"
words = sentence.split()
print(words)    # ['Python', 'is', 'fun']

# join()
new_sentence = " ".join(words)
print(new_sentence) # Python is fun

# replace()
text = "I love Java"
updated_text = text.replace("Java", "Python")
print(updated_text) # I love Python

# strip() - remove whitespace
messy = "     Hello, World!    "
clean_text = messy.strip()
print(clean_text)    # Hello, World!

# Regular Expression for Pattern Matching
import re
text = "Contact me at 123-456-7890"
digits = re.findall(r"\d+", text)
print(digits) # ['123', '456', '7890']

updated_text = re.sub(r"\d", "X", text)
print(updated_text) # Contact me at XXX-XXX-XXXX



