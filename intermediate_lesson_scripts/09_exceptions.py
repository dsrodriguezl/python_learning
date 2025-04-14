# Errors and exceptions
# A python program will terminate if an error is encountered

# There are many error types in python, like the following

# Synthax errors: These occur when the parser detects a synthetically incorrect 
# statement
# E.g. print(1))

# Type error: summing a number and a string (e.g. 5 + "10")

# These error types can help us understand what is wrong with our code. 
# Why does it crash.

# We can raise our own exceptions to prevent edge cases in our code

# x = -5
# if x < 0:
#   raise Exception("x should be positive")

# Another way is to use the assert statement
# assert(x >= 0)

# It is probably more dessirable to make our code handle exceptions, avoiding it
# to terminate if they occur.
# This can be done with try except blocks
try:
  a = 5 / 0
except:
  print("an error happened")

# We can even catch the exception type within a try exception block
try:
  a = 5 / 0
except Exception as e:
  print(e)

# It is a good practice to actually specify the type of exception you want to 
# catch, which requires us to know the possible errors that can occur within our
# code
try:
  a = 5 / 0
  b = a * "10"
except ZeroDivisionError as e:
  print(e)
except TypeError as e:
  print(e)

try:
  a = 5 / 1
  b = a * "10"
except ZeroDivisionError as e:
  print(e)
except TypeError as e:
  print(e)

# We can also include else clauses, for the case no exception occurs
try:
  a = 5 / 1
  b = a + 4
except ZeroDivisionError as e:
  print(e)
except TypeError as e:
  print(e)
else:
  print("Everything is fine")

# We can use a finally clause, which runs no matter is an exception occured or 
# not. This can for exmaple be used for a cleanup operation
try:
  a = 5 / 1
  b = a + 4
except ZeroDivisionError as e:
  print(e)
except TypeError as e:
  print(e)
else:
  print("Everything is fine")
finally:
  print("cleaning up...")

# We can define our own exceptions/error classes
class ValueTooHighError(Exception):
  pass

def test_value(x):
  if x > 100:
    raise ValueTooHighError("Value is to high")

try:
  test_value(200)
except ValueTooHighError as e:
  print(e)

# An example with a custom init method
class ValueTooSmallError(Exception):
  def __init__(self, message, value):
    self.message = message
    self.value = value


def test_value(x):
  if x > 100:
    raise ValueTooHighError("Value is to high")
  if x < 5:
    # In this case we need to pass the value "x"
    raise ValueTooSmallError("Value is to small", x)

try:
  test_value(1)
except ValueTooSmallError as e:
  # We can print both the message and the value
  print(e.message, e.value)


