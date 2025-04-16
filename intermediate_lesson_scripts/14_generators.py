# Generators are functions that retunr an object that can be iterated over
# The itemes within the objects are generated lazylly, so only one at a time
# and when we ask for it
# Therefore, they are very memory efficient than other sequence objects while 
# working with large data sets

# They are defined like normal fucntion but using the yield statement instead 
# of the return statement
def mygenerator():
  # It is possible to have multiple yield statements
  yield 1
  yield 2
  yield 3

g = mygenerator()
# printing the opbjec tonly states that it is a generator
print(g)

## Print values with a loop
for i in g:
  print(i)

## Print values oen at a time
g = mygenerator()
## next takes the value after that of the previous yield operation
value = next(g)
print(value)

value = next(g)
print(value)

value = next(g)
print(value)

# Generators can be used as input for another function that takes iterables
g = mygenerator()
print(sum(g))

g = mygenerator()
print(sorted(g))

# More about the execution of generator
def countdown(num):
  print("Starting")
  while num > 0:
    yield num
    num -= 1

cd = countdown(4)

value = next(cd)
print(value)
value = next(cd)
print(value)
value = next(cd)
print(value)
value = next(cd)
print(value)

# Memory efficiency example
import sys

def firstn(n):
  nums = []
  num = 0
  while num < n:
    nums.append(num)
    num += 1
  return nums

print(firstn(10))
print(sum(firstn(10)))

# Using a generator we do not need to store the list of numbers, thus saving 
# memory
def firstn_generator(n):
  num = 0
  while num < n:
    yield num
    num +=1

print(firstn_generator(10))
print(sum(firstn_generator(10)))

## Size of objects with 1000000 elements in them
### The list and the generator objects differ in size, the generator is smaller
print(sys.getsizeof(firstn(1000000)))
print(sys.getsizeof(firstn_generator(1000000)))

### The sum objects weight the same
print(sys.getsizeof(sum(firstn(1000000))))
print(sys.getsizeof(sum(firstn_generator(1000000))))

# Fibonacci sequence example
def fibonacci(limit):
  # 0 1 1 2 3 5 8 13 ...
  a, b = 0, 1
  while a < limit:
    yield a
    a, b = b, a + b

fib = fibonacci(30)

for i in fib:
  print(i)

# Generator expressions
mygenerator = (i for i in range(10) if i % 2 == 0)
for i in mygenerator:
  print(i)

## This is similar to the list comprehension
mylist = [i for i in range(10) if i % 2 == 0]
print(mylist)

## A generator can be converted to a list
mygenerator = (i for i in range(10) if i % 2 == 0)
print(list(mygenerator))

## size comparison
import sys
mygenerator = (i for i in range(1000000) if i % 2 == 0)
mylist = [i for i in range(1000000) if i % 2 == 0]

print(sys.getsizeof(mygenerator))
print(sys.getsizeof(mylist))
















