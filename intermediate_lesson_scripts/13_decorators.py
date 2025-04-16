# Function decorators
# Functions that take another function as argument and extends its behavior 
# without explicitly modifying it

# The basic synthax is the following:
# @mydecorator
# def dosomething():
#   pass

# Let's try it 
def start_end_decorator(func):
  
  def wrapper():
    print("start")
    func()
    print("end")
  return wrapper

@start_end_decorator
def printname():
  print("Alex")

printname()

@start_end_decorator
def printnum():
  print(5)

printnum()

## If a function performs and operation with an input argument, the args and 
## kwargs notation is needed (this will be explained in a future topic), and
## the result of the operation should be stored and returned by the wrapper
## function of the decorator
def start_end_decorator2(func):
  
  def wrapper(*args, **kwargs):
    print("start")
    result = func(*args, **kwargs)
    print("end")
    return result
  return wrapper

@start_end_decorator2
def add5(x):
  return x + 5

result = add5(10)
print(result)
## This method does not preserve the help and name of the function
print(help(add5))
print(add5.__name__)

## We can use functools to correct it
import functools

def start_end_decorator2(func):
  @functools.wraps(func)
  def wrapper(*args, **kwargs):
    print("start")
    result = func(*args, **kwargs)
    print("end")
    return result
  return wrapper

@start_end_decorator2
def add5(x):
  return x + 5

result = add5(10)
print(result)
print(help(add5))
print(add5.__name__)

# Decorators with arguments
import functools

def repeat(num_times):
  def decorator_repeat(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
      for _ in range(num_times):
        result = func(*args, **kwargs)
      return result
    return wrapper
  return decorator_repeat

@repeat(num_times = 3)
def greet(name):
  print(f"Hello {name}")

greet("Alex")

# Nested decorators
import functools

def start_end_decorator3(func):
  @functools.wraps(func)
  def wrapper(*args, **kwargs):
    print("start")
    result = func(*args, **kwargs)
    print("end")
    return result
  return wrapper

def debug(func):
  @functools.wraps(func)
  def wrapper(*args, **kwargs):
    args_repr = [repr(a) for a in args]
    kwargs_repr = [f"{k} = {v!r}" for k, v in kwargs.items()]
    signature = ", ".join(args_repr + kwargs_repr)
    # Print information of the function
    print(f"Calling {func.__name__}({signature})")
    # Execute function and store result
    result = func(*args, **kwargs)
    # Print information about the value returned by the function
    print(f"{func.__name__!r} returned {result!r}")
    return result
  return wrapper

## If mutliple decorators are applied to a function they are executed in the 
## order they are listed
## The debug decorator calls the function thus the start_end_decorator3 within 
## its own execution
@debug
@start_end_decorator3
def greet(name):
  greeting= f"Hello {name}"
  print(greeting)
  return greeting

greet("Alex")

# class decorators
# Are similar to function decorators but they are typically used in the case we
# want to mantain and update a state
## In the following example we want totrack the times we have executed a 
## function
class CountCalls:
  def __init__(self, func):
    self.func = func
    self.num_calls = 0
  
  # For a classs decorator we need to implement the __call__ method
  ## This is the same as the function within a function decorator
  ## It allows us to execute an object of the specified class
  def __call__(self, *args, **kwargs):
    self.num_calls = self.num_calls + 1
    print(f"This is executed {self.num_calls} times")
    # Execute and return the function
    return self.func(*args, **kwargs)

@CountCalls
def say_hello():
  print("Hello")

say_hello()
say_hello()

for i in [1,2,3]:
  say_hello()
