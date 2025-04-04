# We can do basically any kind of nummeric operatiosn in python
# Print any number
print(1)
print(1.5)
print(-1.5)

# Perform arithmetics
print(2 - 1.5)
print(2 * 1.5)
print(2 * 4 + 5)
print(2 * (4 + 5))

# Modulus operation. Remainder of 10/3
print(10 % 3)

# Variables
my_num = 5
print(my_num)

#Transform them into strings
print(str(my_num))

# Now we can add the number to a string, because it gets transformed into one
print(str(my_num) + " things")

# Obtain absoulte values
print(abs(my_num))

# 3^2
print(pow(3,2))

# Find the biggest one
print(max(1, 2, 3, 5, 10))

# Round
print(round(3.4))

# Let's import some functions to do even more operations
from math import *

print(floor(3.7))
print(ceil(3.7))
print(sqrt(36))
