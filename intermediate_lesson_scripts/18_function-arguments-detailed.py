"""
- Difference between arguments and parameters
- Positional and keyword arguments
- Default arguments
- Variable-length arguments (*args and **kwargs)
- Container unpacking into function arguments
- Loval vs. global arguments
- Parameter passing (by value or by reference?)
"""

# Parameters are the variabel defined or used inside () in a function definition
# Arguments are the values passed for the parameters while calling a fucntion
def print_name(name):
  print(name)

print_name("Alex")
## name is the parameter, Alex is the argument

# Positional and keyword arguments
def foo(a, b, c):
  print(a, b, c)

## positional arguments
### ORDER MATTERS
foo(1, 2, 3)

## keyword arguments
### ORDER IS IRRELEVANT
foo(a = 1, b = 2, c = 3)
foo(b = 2, a = 1, c = 3)
foo(b = 2, c = 3, a = 1)

# Default arguments
## PRedefined values for the parameters that can be changed by the user when 
## callign the function, if needed
## default arguments should be defined for the last parameters of the fucntion
def foo(a, b, c, d = 4):
  print(a, b, c, d)

foo(1, 2, 3)
foo(1, 2, 3, 7)

# Variable-length arguments
## If a parameter is marked with * any number of positional arguments (args) can
## be passed to the function
## If a parameter is marked with ** any number of keywords arguments (kwargs)
## can be passed to the function
## args and kwargs are typical names for these parameters, but they can be 
## called any way you want
def foo(a, b, *args, **kwargs):
  print(a, b)
  # The args argument is defined as a tuple within the function
  for arg in args:
    print(arg)
    
  # the kwargs arguemnt is defined as a dictionary within the function
  for key in kwargs:
    print(key, kwargs[key])

## 1 and 2 are positional arguments for a and b
## 3, 4, and 5 are positionala rguments for args
## the keyword arguments 6 and 7 are taken by the kwargs parameter
foo(1, 2, 3, 4, 5, six = 6, seven = 7)

## we can skip the args if needed
foo(1, 2, six = 6, seven = 7)

## we can pass more positional arguments for args, without passing arguments 
## for kwargs
foo(1, 2, 3, 4, 5, 6, 7)

## forced keyword arguments
### allowing only keyword arguments
def foo(a, b, *, c, d):
  print(a, b, c, d)
## parameters after the * must be passed keyword arguments or the fucntion 
## crashes with an error
foo(1, 2, c = 3, d = 4)

"""
error crashing code and its returned error:
foo(1,2,3,4)
Error in py_run_file_impl(file, local, convert) : 
  TypeError: foo() takes 2 positional arguments but 4 were given
"""
## same can be achieved with *args
def foo(*args, last):
  for arg in args:
    print(arg)
  print(last)

foo(1, 2, 3, last = 4)


# Unpacking arguments
def foo(a, b, c):
  print(a, b, c)

my_list = [0, 1, 2]

## We can unpack the list into the arguments of the function
foo(*my_list)

## It also works with tuples
my_tuple = (0, 1, 2)
foo(*my_tuple)

## In case of a dictionary the keys must match that of the keyword parameters
## and we need to use ** for keyword arguments
my_dict = {"a": 1, "b": 2, "c": 3}
foo(**my_dict)

# Local vs. global variables
def foo():
  # Access global variable
  x = number
  print("number inside fucntion:", x)

## define a global variable
number = 0
foo()


## modifying a global variable within a function
def foo():
  global number
  x = number
  number = 3
  print("number inside fucntion:", x)

print(number)
foo()
print(number)

# Parameter passing (by value or by reference?)
# In python the mechanism is called called by object or called by object 
# reference
# How are arguments passed to a function and how can the function change their
# values?

# Explanation within examples

# Ex. 1
def foo(x):
  x = 5

var = 10
foo(var)

## var remains as 10 even if it gets assigned a value 5 within foo
## because an integer is immutable
## so far is the same as local and global objects
print(var)

# Ex. 2
def foo(a_list):
  a_list.append(4)

my_list = [1,2,3]
foo(my_list)

## lists can be modified within a function because they are mutable
print(my_list)

# Ex. 3
def foo(a_list):
  a_list.append(4)
  a_list[0] = -100

my_list = [1,2,3]
foo(my_list)
## immutable objects within mutabel objects can also be changed within a 
## function
print(my_list)


# Ex. 4
def foo(a_list):
  # Rebinding the mutable reference
  ## This creates a local variable
  a_list = [200, 300, 400]
  a_list.append(4)
  a_list[0] = -100

my_list = [1,2,3]
foo(my_list)
## If rebinding the global list within the function, the global variable remains
## unchanged, as the rebindign within the function created a local variable
print(my_list)

# Ex. 5
def foo(a_list):
  a_list += [200, 300, 400]

my_list = [1,2,3]
foo(my_list)
## The function did not create a local variable, thus affected the list
print(my_list)

def foo(a_list):
  a_list = a_list + [200, 300, 400]

my_list = [1,2,3]
foo(my_list)
## The function did create a local variable, thus did not affect the list
print(my_list)
