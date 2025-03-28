# Strings correspond to plain text data. One of the most common types of data
# to work with python.

# \n inserts a new line within a string
print("Giraffe \nAcademy")

# \ is called the scape character. It allows to use special characters within a 
# string.
print("Giraffe \"Academy\"")

# it can aslo jus tbe used as a normal \
print("Giraffe \Academy")

# String concatenation example, sotring a strign within a variable
phrase = "Giraffe Academy"
print(phrase + " is cool")

# Using functions with strings.
# transform it to lower or upper case
print(phrase.lower())
print(phrase.upper())

# Verify if it is in upper case
print(phrase.isupper())

# Transform to upper case and verify if it is in upper case
print(phrase.upper().isupper())

# Count characters in it
print(len(phrase))

# Subset a string
# Note: coutning in python starts at 0, not 1.
# Grab the first character
print(phrase[0])

# grab characters in a range
print(phrase[0:5])

# Locate the position of a chracter (or set of them) within the string
print(phrase.index("G"))
print(phrase.index("a"))
print(phrase.index("f"))
print(phrase.index("Acad"))
print(phrase.index(" "))

# Replace values within a string
print(phrase.replace("Giraffe", "Elephant"))
