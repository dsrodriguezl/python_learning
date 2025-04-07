# Lists: Ordered, mutable, and allow duplicate elements
mylist = ["banana", "cherry", "apple"]
print(mylist)

# Empty lists can be created with the list function
mylist2 = list()
print(mylist2)

# Lists allow for different data types
mylist3 = [2, True, "apple", "apple"]
print(mylist3)

# To access elements from a list, we refer to its index
item = mylist[1]
print(item)

item = mylist[-1]
print(item)

for i in mylist:
  print(i)

# Chek if an item is in a list
if "banana" in mylist:
  print("Yes")
else:
  print("No")

if "lemon" in mylist:
  print("Yes")
else:
  print("No")

# How many elements in a list?
print(len(mylist))

# Append an item to a list
print(mylist)
mylist.append("lemon")
print(mylist)

# Insert an item in a spacific position within a list
mylist.insert(1, "blueberry")
print(mylist)

# Remove the last item from a list
item = mylist.pop()
# pop takes and removes the last item from a list
print(item)
print(mylist)

# Remove a specific item
mylist.remove("cherry")
print(mylist)

# Empty a list
mylist.clear()
print(mylist)

# Reverse a list
mylist = ["banana", "cherry", "apple"]
print(mylist)
mylist.reverse()
print(mylist)

# Sort items in a list
mylist4 = [4, 5, 1, -1]
print(mylist4)
mylist4.sort()
print(mylist4)

mylist4 = [4, 5, 1, -1]
new_list = sorted(mylist4)
print(mylist4)
print(new_list)

# A list with the same elements multiple times
mylist5 = [0] * 5
print(mylist5)

# Concatenate lists
new_list = mylist + mylist5
print(new_list)

# Slicing/subsetting
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(mylist)

## Specific range
a = mylist[1:5]
print(a)

## All the way up to an item
a = mylist[:5]
print(a)

## All the way from an item
a = mylist[1:]
print(a)

## By steps
a = mylist[::1]
print(a)

a = mylist[::2]
print(a)

## A different way to reverse a list
a = mylist[::-1]
print(a)

# Copy a list
fruits = ["banana", "cherry", "apple"]

fruits_copy = fruits
print(fruits_copy)

## With this method, if the copy is modified, the original list will also be
## modified accordingly
fruits_copy.append("lemon")
print(fruits_copy)
print(fruits)

## To avoid this, we can use the copy function
fruits_copy = fruits.copy()
fruits_copy.append("orange")
print(fruits_copy)
print(fruits)

## OR using the list function
fruits_copy = list(fruits)
fruits_copy.append("orange")
print(fruits_copy)
print(fruits)

## OR by slicing all the way from the beginning to the end of the original list
fruits_copy = fruits[:]
fruits_copy.append("orange")
print(fruits_copy)
print(fruits)

# List comprehension: Elegant and fast way to create a new list from an
# existing one, with a signle line of code
print(mylist)

## The new list will contain the squares of the numbers in mylist
new_list = [i*i for i in mylist]
print(new_list)

