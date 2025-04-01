# for loops allow itereatign code through a collection of values

# Iterate through the values/characters of a string, pritning them
for letter in "Giraffe Academy":
  print(letter)

# Iterate through values in an array
friends = ["Jim", "Karen", "Kevin"]
for friend in friends:
  print(friend)

# Iterate through a series of numbers
for index in range(10):
  print(index)

for index in range(3, 10):
  print(index)

# The series of numbers can be determined by the length of another variable
for index in range(len(friends)):
  print(index)

# The indexes can be used to print the values they correspond to
for index in range(len(friends)):
  print(friends[index])

# For loops can be used to perform any type of operations
for index in range(5):
  if index == 0:
    print("First itereation")
  else:
    print("Not first iteration")
