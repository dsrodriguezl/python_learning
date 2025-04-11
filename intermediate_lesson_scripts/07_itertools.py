# itertools: Is a module with a collection of tools for handling iterators.
# Iterators are data types that can be used in a for loop.
# itertools: product, permutations, combinations, accumulate, groupby, and 
# infinite iterators

# Product
from itertools import product
a = [1, 2]
b = [3, 4]
prod = product(a, b)
## This combines the element of both lists
print(list(prod))

## We can set the number of repetitions
prod = product(a, b, repeat = 2)
print(list(prod))

### This produces an very long output, let's try combinin a with a shorter list
### to better see the effect of the addedd repetitions
c = [3]
prod = product(a, c, repeat = 2)
print(list(prod))

# Permutations
from itertools import permutations
a = [1, 2, 3]
perm = permutations(a)
## This returns all possible orderings of the elements in the list
print(list(perm))

## We can specify the length of the permutations
perm = permutations(a, 2)
print(list(perm))

# Combinations
from itertools import combinations
a = [1, 2, 3, 4]
comb = combinations(a, 2)
## This makes all the possible combinations with a specified length
print(list(comb))

## Note no combinations are made with the same elements (e.g. (1,1))
## This can be achieved with the combinations_with_replacement function
from itertools import combinations_with_replacement
comb_wr = combinations_with_replacement(a, 2)
print(list(comb_wr))

# Accumulate
from itertools import accumulate
a = [1, 2, 3, 4]
acc = accumulate(a)
## This returns the accumulated sums or any other specified binary operation
print(a)
print(list(acc))

## accumulated product
import operator
acc = accumulate(a, func = operator.mul)
print(a)
print(list(acc))

## accumulated maximum
a = [1, 2, 5, 3, 4]
acc = accumulate(a, func = max)
print(a)
print(list(acc))

# Groupby
from itertools import groupby

## function to apply for the determination of the group keys
def smaller_than_3(x):
  return x < 3

a = [1, 2, 3, 4]
group_ob = groupby(a, key = smaller_than_3)
## This returns keys and groups from the list, according to the applied funtion
## for the determination of the group keys
for key, value in group_ob:
  print(key, list(value))

### Alternatively a lambda function can be used for the keys
group_ob = groupby(a, key = lambda x: x < 3)
for key, value in group_ob:
  print(key, list(value))

## Another example grouping people by age
persons = [
  {"name": "Tim", "age": 25}, {"name": "Dan", "age": 25},
  {"name": "Lisa", "age": 27}, {"name": "Claire", "age": 28}
]
group_ob = groupby(persons, key = lambda x: x["age"])
for key, value in group_ob:
  print(key, list(value))

# Infinite iterators
from itertools import count, cycle, repeat

## count
### It creates an infinite count by the specified steps
#### Example printin counts by 10 up to 15
for i in count(10):
  print(i)
  # Without this break, the code will count infinitely
  if i == 15:
    break

## cycle
### It cycles infinetly through an iterable
a = [1, 2, 3]
#### Example cycling through the list once
for i in cycle(a):
  print(i)
  # Without this break, the code will cycle infinitely
  if i == 3:
    break

## repeat
### It repeats infinetly. Accepts a stop repetition as a second argument
#### Examples repeating 4 time one  and the list a
for i in repeat(1, 4):
  print(i)

for i in repeat(a, 4):
  print(i)



