# Strings: Ordered, immutable, text representations
mystring = "Hello world"
print(mystring)

mystring = 'Hello world'
print(mystring)

mystring = 'I\'m a programmer'
print(mystring)

mystring = "I'm a programmer"
print(mystring)

# Multiline string
mystring = """Hello 
world"""
print(mystring)

# Avoid new lines in a strign specified in multiple code lines
mystring = """Hello \
world"""
print(mystring)

# Subset
mystring = "Hello world"
print(mystring)
char = mystring[0]
print(char)
char = mystring[1]
print(char)
char = mystring[2]
print(char)
char = mystring[-1]
print(char)
char = mystring[-2]
print(char)

## ranges
substring = mystring[1:5]
print(substring)

substring = mystring[1:]
print(substring)

substring = mystring[:5]
print(substring)

substring = mystring[:]
print(substring)

### stepped ranges
substring = mystring[::]
print(substring)

substring = mystring[::2]
print(substring)

## reversing the string
substring = mystring[::-1]
print(substring)

# Concatenate strings
greeting = "Hello"
name = "Tom"
sentence = greeting + name
print(sentence)
sentence = greeting + " " + name
print(sentence)

# Iterate through a string
for i in greeting:
  print(i)

# Check if a character or substring is within a string
if "e" in greeting:
  print("YES")
else:
  print("NO")

if "o" in greeting:
  print("YES")
else:
  print("NO")

if "ell" in greeting:
  print("YES")
else:
  print("NO")

# Remove white space on the edges of a string
mystring = "  Hello World  "
print(mystring)
## As strings are immutable we cannot modify them in place, so we have to 
## redefine them
mystring = mystring.strip()
print(mystring)

#  Modify the case
mystring = "Hello World"
print(mystring.upper())
print(mystring.lower())

# Check start or end
print(mystring.startswith("H"))
print(mystring.startswith("l"))
print(mystring.startswith("Hello"))
print(mystring.startswith("World"))

print(mystring.endswith("H"))
print(mystring.endswith("l"))
print(mystring.endswith("Hello"))
print(mystring.endswith("World"))

# Find substrings or characters first position
print(mystring.find("World"))
print(mystring.find("o"))

# Count the times a character or substring is present
print(mystring.count("o"))
print(mystring.count("l"))
print(mystring.count("p"))
print(mystring.count("ll"))
print(mystring.count("orld"))


# Replace characters or substrings within a string
print(mystring.replace("World", "Universe"))
print(mystring.replace("Wolrd", "Universe"))

# Convert to a list
mystring = "how, are, you. doing"
print(mystring)
mylist = mystring.split()
print(mylist)
mylist = mystring.split(" ")
print(mylist)
mylist = mystring.split(",")
print(mylist)
mylist = mystring.split(".")
print(mylist)

# Convert list to string
mylist = mystring.split()
print(mylist)

newstring = "".join(mylist)
print(newstring)
newstring = " ".join(mylist)
print(newstring)
newstring = ",".join(mylist)
print(newstring)
newstring = ".".join(mylist)
print(newstring)
newstring = " ,".join(mylist)
print(newstring)

## Let's expand on this method
### We want to convert a list into a string
mylist = ["a"] * 100
print(mylist)

### An alternative is to use a for loop
### The problem with the for loop is that it is creating a new string in each 
### iteration, so is  a waste of resourses
mystring = ""

from timeit import default_timer as timer

start = timer()
for i in mylist:
  # This is the same as mystring = mystring + i
  mystring += i
print(mystring)
stop = timer()
print(stop - start)

### A more efficient alternative to the for loop is using the .join method of 
### before, which is also a more compact code
start = timer()
mystring = "".join(mylist)
print(mystring)
stop = timer()
print(stop - start)

# Format strings
var = "Tom"
var2 = 3
var3 = 3.123456

##  % method (old)
### Using a string varaible %s
mystring = "the variable is %s" % var
print(mystring)

### Using a numeric variable %d (integers) o r %f (floats)
mystring = "the variable is %d" % var2
print(mystring)

mystring = "the variable is %d" % var3
print(mystring)

mystring = "the variable is %f" % var3
print(mystring)

mystring = "the variable is %f" % var2
print(mystring)

mystring = "the variable is %.2f" % var3
print(mystring)

mystring = "the variable is %.9f" % var3
print(mystring)

## .format() method (new)
mystring = "the variable is {}".format(var)
print(mystring)

mystring = "the variable is {}".format(var2)
print(mystring)

mystring = "the variable is {}".format(var3)
print(mystring)

mystring = "the variable is {:.2f}".format(var3)
print(mystring)

mystring = "the variable is {:.9}".format(var3)
print(mystring)

mystring = "the variable is {:.2f} and {}".format(var3, var)
print(mystring)

## f-Strings method (newest)
mystring = f"the variable is {var}, {var2}, and {var3}"
print(mystring)

mystring = f"the variable is {var*2}, {var2*2}, and {var3*2}"
print(mystring)
