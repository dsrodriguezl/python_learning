lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

# extend allows us to append a list onto the end of a list
friends.extend(lucky_numbers)
print(friends)

# append can be used to append a values onto a list
friends.append("Creed")
print(friends)

# insert allows us to insert a vlaue in a specific index position within a list
friends.insert(2, "Kelly")
print(friends)

# remove allows us to remove any element from a list
friends.remove("Jim")
print(friends)

# clear allows removing all entries of a list
friends.clear()
print(friends)

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

# pop removes the last element of a list
print(friends)
friends.pop()
print(friends) 

# index can be used to find the index position of an entry
print(friends.index("Kevin"))

# Count can be used to count the number of similar elements in a list
friends = ["Kevin", "Karen", "Jim", "Jim", "Jim", "Oscar", "Toby"]
print(friends.count("Jim"))

# sort allows sorting a list in ascending order
friends.sort()
print(friends)

lucky_numbers = [4, 15, 16, 8, 23, 42]
lucky_numbers.sort()
print(lucky_numbers)

# reverse reverts the order of the entries of a list
lucky_numbers.reverse()
print(lucky_numbers)

# copy allows copying a list
friends2 = friends.copy()
print(friends2)
