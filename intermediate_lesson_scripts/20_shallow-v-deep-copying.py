org = 5
cpy = org
# Instead of a copy we made a new variable with the same reference
## This is not a problem with immutable objects like this integer
cpy = 6
print(cpy)
print(org)

## with mutables like lists, this can be problematic
org = [0, 1, 2, 3, 4]
cpy = org
cpy[0] = -10
## Both changed!
print(cpy)
print(org)

# To make real copies the copy module is required
import copy
## Shallow copy: One level ddep, only references of nested child objects
## Deep copy: Full independent copy

## Shallow
org = [0, 1, 2, 3, 4]
cpy = copy.copy(org)
cpy[0] = -10
## Only the copy changed
print(cpy)
print(org)

### Several options for shallow copying a list
cpy = org.copy()
cpy[0] = -10
## Only the copy changed
print(cpy)
print(org)

cpy = list(org)
cpy[0] = -10
## Only the copy changed
print(cpy)
print(org)

cpy = org[:]
cpy[0] = -10
## Only the copy changed
print(cpy)
print(org)

### What about nested lists?
org = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
cpy = copy.copy(org)
cpy[0][0] = -10
## Both changed! it is a shallow copy (only one level deep)
print(cpy)
print(org)

## Deep
org = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
cpy = copy.deepcopy(org)
cpy[0][0] = -10
## Only the copy changed
print(cpy)
print(org)

# These methods can also be used in custom objects
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Alex", 27)
p2 = p1

p1.age = 28
## Both changed, because we did not produce a real copy
print(p2.age)
print(p1.age)

p1 = Person("Alex", 27)
p2 = copy.copy(p1)

p1.age = 28
## Original is not changed!
print(p2.age)
print(p1.age)

### deeper structure case
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

class Company:
  def __init__(self, boss, employee):
    self.boss = boss
    self.employee = employee

p1 = Person("Alex", 55)
p2 = Person("Joe", 27)

company = Company(p1, p2)
company_clone = copy.copy(company)

company_clone.boss.age = 56
print(company_clone.boss.age)
## Both changed, age is at level 2
print(company.boss.age)


p1 = Person("Alex", 55)
p2 = Person("Joe", 27)

company = Company(p1, p2)
company_clone = copy.deepcopy(company)

company_clone.boss.age = 56
print(company_clone.boss.age)
## Original remains unchanged!
print(company.boss.age)
