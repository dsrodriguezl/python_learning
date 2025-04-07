# Sets: Unordered, mutable, no duplicates allowed
myset = {1, 2, 3, 1, 2}
print(myset)

myset = set([1, 2, 3])
print(myset)

myset = set("Hello")
print(myset)

# Create an empty set
## Wrong
myset = {}
print(type(myset))

## Right
myset = set()
print(type(myset))

# Add elements
myset = set()
myset.add(1)
myset.add(2)
myset.add(3)
print(myset)

# Remove elements
myset.remove(3)
print(myset)

myset.discard(2)
print(myset)

## Unlike rmeove, discard does not fail, no error is returned stoppign the code,
## if we attempt to remove an unexisting element
myset.discard(2)
print(myset)

## Empty a set
myset.add(2)
myset.add(3)
print(myset)

myset.clear()
print(myset)

## Return the first value from a set, while removing it from the set
myset.add(1)
myset.add(2)
myset.add(3)
print(myset)

print(myset.pop())
print(myset)

# Iterate through a set

for i in myset:
  print(i)

# Check if an element is in the set
if 1 in myset:
  print("Yes")
else:
  print("No")

if 2 in myset:
  print("Yes")
else:
  print("No")

# Union and intersection of sets
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

## A union combines the elements of two sets without duplciation
u = odds.union(evens)
print(u)

u = odds.union(primes)
print(u)

## An intersection only takes elements from both sets
i = odds.intersection(evens)
print(i)

i = odds.intersection(primes)
print(i)

i = evens.intersection(primes)
print(i)

# Difference between sets
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

## Elements in A that are not in B
diff = setA.difference(setB)
print(diff)

## Elements in B that are not in A
diff = setB.difference(setA)
print(diff)

## Elements that are not shared between sets
diff = setA.symmetric_difference(setB)
print(diff)

diff = setB.symmetric_difference(setA)
print(diff)

# Modify a set in place
## Union
setA.update(setB)
print(setA)

## Intersection
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
setA.intersection_update(setB)
print(setA)

## Differences
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
setA.difference_update(setB)
print(setA)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
setA.symmetric_difference_update(setB)
print(setA)

# Subsets and supersets
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3}

## Is a set a subset of the other?
print(setA.issubset(setB))
print(setB.issubset(setA))

## Is a set a superset of the other?
print(setA.issuperset(setB))
print(setB.issuperset(setA))

# Are two sets disjoint? So,they do not share elements
setC = {7, 8, 9}
print(setA.isdisjoint(setB))
print(setB.isdisjoint(setA))
print(setA.isdisjoint(setC))
print(setB.isdisjoint(setC))

# Copy sets
setA = {1, 2, 3, 4, 5, 6}
setB = setA
print(setB)
## This methoda has the issue that modifications on the copy are passed to the
## original
setB.add(7)
print(setB)
print(setA)

## This can be avoided with the copy function
setA = {1, 2, 3, 4, 5, 6}
setB = setA.copy()
print(setB)
setB.add(7)
print(setB)
print(setA)

## Alternatively, we can use the set fucntion
setB = set(setA)
print(setB)
setB.add(7)
print(setB)
print(setA)

# Frozen set: inmutable version of a set
a = frozenset([1, 2, 3, 4])
print(a)

## As they are inmutable, elements cannot be added nor removed from them after
## their creation


