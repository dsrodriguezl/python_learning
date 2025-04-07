# Tuple: ordered, inmutable, allows duplicate elements
mytuple = ("Max", 28, "Boston")
print(mytuple)

# The parentehses are optional
mytuple = "Max", 28, "Boston"
print(mytuple)
 
# Tuples with only one element need a comma at the end within the parenthesis
mytuple = ("Max",)
print(mytuple)

# The tuple function can be used to create a tuple from an iterable, like a list
mytuple = tuple(["Max", 28, "Boston"])
print(mytuple)
print(type(mytuple))

# To access elements withina  tuple we refer to their indexes
item = mytuple[1]
print(item)
item = mytuple[0]
print(item)
item = mytuple[-1]
print(item)
item = mytuple[-2]
print(item)

for i in mytuple:
  print(i)

item = mytuple[1]
print(item)

# Check if an element is inside a tuple
if "Max" in mytuple:
  print("Yes")
else:
  print("No")

if "Fred" in mytuple:
  print("Yes")
else:
  print("No")

# How many elements in a tuple?
print(len(mytuple))

# Count some elements in a tuple
mytuple = ("a", "p", "p", "l", "e")
print(mytuple.count("p"))
print(mytuple.count("x"))

# Find first index of a specific element in a tuple
print(mytuple.index("p"))
print(mytuple.index("l"))

# Convert a tuple into a list and vice versa
mylist = list(mytuple)
print(mylist)

mytuple2 = tuple(mylist)
print(mytuple2)

# Slicing/subsetting
a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

## Within a range
b = a[2:5]
print(b)

b = a[:5]
print(b)

b = a[2:]
print(b)

b = a[::1]
print(b)

b = a[::2]
print(b)

### A way to reverse a tuple
b = a[::-1]
print(b)

# Unpacking
mytuple = ("Max", 28, "Boston")

# note: the number of relement on the left must match the length of the tuple
name, age, city = mytuple
print(name)
print(age)
print(city)

# Mutlipple elements can be unpacked within a single object using *
name, *age_city = mytuple
print(name)
print(age_city)

*name_age, city = mytuple
print(name_age)
print(city)

name, *age_city = mytuple
print(name)
print(age_city)

# Tuples vs lists
# As tuples are unmutables, python can perform some internal optimizations that
# can make the computations with tuples more efficient
import sys
mylist = [0, 1, 2, "hello", True]
mytuple = (0, 1, 2, "hello", True)
print(sys.getsizeof(mylist), "bytes")
print(sys.getsizeof(mytuple), "bytes")

import timeit
print(timeit.timeit(stmt = "[0, 1, 2, 3, 4, 5]", number = 100000))
print(timeit.timeit(stmt = "(0, 1, 2, 3, 4, 5)", number = 100000))
