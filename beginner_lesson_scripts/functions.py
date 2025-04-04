# Functions are code collections that perform specific tasks
# We can define our own functions
def say_hi():
  print("Hello user")

# To execute the code of a function we need to call it
say_hi()

# We can specify parameters required for the functions to work
def say_hi(name):
  print("Hello " + name)

say_hi("Daniel")

#  We can specify as many parameters as we want/need
def say_hi(name, age):
  print("Hello " + name + ", you are " + str(age))

say_hi("Daniel", 18)
