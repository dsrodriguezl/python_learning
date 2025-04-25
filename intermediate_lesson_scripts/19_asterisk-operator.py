# multiplication
result = 5 * 7
print(result)

# power
result = 2 ** 4
print(result)

# lists with repeated elements
my_list = [0] * 10
print(my_list)

my_list = [0, 1] * 10
print(my_list)

# tuples
my_tuple = (0,) * 10
print(my_tuple)

my_tuple = (0,1) * 10
print(my_tuple)

# strings
my_string = "AB" * 10
print(my_string)

# *args and **kwargs
def foo(a, b, *args, **kwargs):
  print(a, b)
  for arg in args:
    print(arg)
  for key in kwargs:
    print(key, kwargs[key])

foo(1, 2, 3, 4, 5, six = 6, seven = 7)

# keyword argument enforcement
def foo(a, b, *, c):
  print(a, b, c)

foo(1, 2, c = 3)

# argument unpacking
def foo(a, b, c):
  print(a, b, c)

my_list = [0, 1, 2]
foo(*my_list)

# unpacking containers
my_list = [1, 2, 3, 4, 5, 6]

*beginning, last = my_list
print(beginning)
print(last)

beginning, *last = my_list
print(beginning)
print(last)

beginning, *middle, last = my_list
print(beginning)
print(middle)
print(last)

beginning, *middle, secondlast, last = my_list
print(beginning)
print(middle)
print(secondlast)
print(last)

## This always unpacks into lists
my_tuple = (1, 2, 3, 4, 5, 6)
*beginning, last = my_tuple
print(beginning)
print(last)

# Merge iterables into a list
my_tuple = (1, 2, 3)
my_list = [4, 5, 6]

new_list = [*my_tuple, *my_list]
print(new_list)

my_tuple = (1, 2, 3)
my_set = {4, 5, 6}

new_list = [*my_tuple, *my_set]
print(new_list)

# Merge dictionaries
dict_a = {"a": 1, "b": 2}
dict_b = {"c": 3, "d": 4}

my_dict = {**dict_a, **dict_b}
print(my_dict)
