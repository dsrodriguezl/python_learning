# lambda: Small one line anonymous functions.
# They have the following structure "lambda arguments: expression"
add10 = lambda x: x + 10
print(add10(5))

# This is equivalent to the following function
def add10_func(x):
  return x + 10

print(add10_func(5))
# lambda functions can receive multiple arguments
mult = lambda x, y: x * y
print(mult(2,3))

# lambda functions are typically used when a simple function is required for a
# single usage within a code, or as an argument to hire other fucntions (
# functions that take other functions as arguments)

## Examples sorting
points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
### BY default this sorts the list by the first entry (index 0) of the tuples it 
### contains
points2D_sorted = sorted(points2D)
print(points2D)
print(points2D_sorted)

### We can use a key argument to change the default sorting method
#### Here we usa a lambda function as the key to sort by the second entry of the 
#### tuples (index 1)
points2D_sorted = sorted(points2D, key = lambda x: x[1])
print(points2D)
print(points2D_sorted)

#### This could also be done with a classical function
def sort_by_y(x):
  return x[1]

points2D_sorted = sorted(points2D, key = sort_by_y)
print(points2D)
print(points2D_sorted)

### Sorting by the sum of the elements in the tuples
points2D_sorted = sorted(points2D, key = lambda x: x[0] + x[1])
print(points2D)
print(points2D_sorted)

# Example with the map function
## map function transforms each elements with another fucntion
## I t maps a function along a collection
a = [1, 2, 3, 4, 5]
## Each element in a is multiplied by 2 to define a new list b
b = map(lambda x: x * 2, a)

print(a)
print(b)
print(list(b))

## This could also have been achieved via list comprehesion, which might be the
## most efficient approach for this specific operation, but this example
## Is here to illustrate the usage of lambda within map functions
c = [x * 2 for x in a]
print(c)

# Example with filter
## filter returns all elements in a collection for which a functions returns 
## True
a = [1, 2, 3, 4, 5, 6]
# Obtaining the even numbers (divisible by 2)
b = filter(lambda x: x % 2 == 0, a)
print(list(b))

## This could also have been achieved with list comprehesions, but this example
## fulfills its illustrative purposes
c = [x for x in a if x % 2 == 0]
print(c)

# Example with reduce
## reduce repeatedly applies a function to the elements of a collectable, 
## returning a single value
from functools import reduce
print(a)
# Get the product of all elements in a
product_a = reduce(lambda x, y: x * y, a)
print(product_a)

