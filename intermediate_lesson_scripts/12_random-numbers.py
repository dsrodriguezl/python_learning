# pseudorandom numbers with the random module
import random

## Single float between 0 and 1
a = random.random()
print(a)

## Single float within specific range
a = random.uniform(1, 10)
print(a)

## Single integer within specific range
a = random.randint(1, 10)
print(a)

## Single integer within specific range, without the upper bound
a = random.randrange(1, 10)
print(a)

## From a normal distribution with (mean, sd)
a = random.normalvariate(0, 1)
print(a)

## Working with sequences
mylist = list("ABCDEFGH")
print(mylist)

### Pick one random element
a = random.choice(mylist)
print(a)

### Pick several random elements, without replacement
a = random.sample(mylist, 3)
print(a)

### Pick several random elements, with replacement
a = random.choices(mylist, k = 3)
print(a)

### Shuffle the elements
random.shuffle(mylist)
print(mylist)

## We can choose a seed for the random numbers generator for reproducibility
random.seed(123456)
print(random.random())
print(random.randint(1,10))

random.seed(123456)
print(random.random())
print(random.randint(1,10))

random.seed(1234567)
print(random.random())
print(random.randint(1,10))

## As pseudorandom numbers are reproducible, they are not recommended for 
## security purposes

# Cryptographically strong random numbers with the secrets module
# The functions of this module are recommended for security purposes like 
# passwords, security tokens, etc.
import secrets

## Random integer from 0 to an upper bound, not including the upper bound
a = secrets.randbelow(10)
print(a)

## Random integer with k random bits
a = secrets.randbits(4)
print(a)

## Secret choice
mylist = list("ABCDEFGH")
a = secrets.choice(mylist)
print(a)

# Generate arrays with random number using the numpy random module
import numpy as np

## random array with specified dimensions
### 3D
a = np.random.rand(3)
print(a)

### 5D
a = np.random.rand(5)
print(a)

### 3 X 3
a = np.random.rand(3, 3)
print(a)

## array with random integers in a range
### 3D array with random integers between 0 and 10, without the upper bound
a = np.random.randint(0, 10, 3)
print(a)

### 3 X 4 array with random integers between 0 and 10, without the upper bound
a = np.random.randint(0, 10, (3, 4))
print(a)

## shuffle
np.random.shuffle(a)
print(a)

## numpy random generator uses is different to that of the random module
## so, it uses a different seed
np.random.seed(1)
print(np.random.rand(3, 3))
np.random.seed(1)
print(np.random.rand(3, 3))
np.random.seed(2)
print(np.random.rand(3, 3))


