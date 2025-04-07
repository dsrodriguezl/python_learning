# Dictionary: Key-Value pairs, Unordered, Mutable

# We create them with {}
mydict = {
  "name": "Max",
  "age": 28,
  "city": "New York"
}
print(mydict)

# We can also use the dict function to create them
mydict2 = dict(name = "Mary", age = 27, city = "Boston")
print(mydict2)

# Access values within a dictionary
value = mydict["name"]
print(value)

value = mydict2["name"]
print(value)

# Add values
mydict["email"] = "max@xyz.com"
print(mydict)

# If key already exists, the value is overwritten
mydict["email"] = "coolmax@xyz.com"
print(mydict)

# Delete values
del mydict["name"]
print(mydict)

mydict.pop("age")
print(mydict)

mydict.popitem()
print(mydict)

# Check if a key already exists
mydict = {
  "name": "Max",
  "age": 28,
  "city": "New York"
}
print(mydict)

if "name" in mydict:
  print(mydict["name"])

if "lastname" in mydict:
  print(mydict["lastname"])

try:
  print(mydict["name"])
except:
  print("Error")

try:
  print(mydict["lastname"])
except:
  print("Error")

# Loop through a dictionary
for key in mydict:
  print(key)

for key in mydict.keys():
  print(key)

for value in mydict.values():
  print(value)

for key, value in mydict.items():
  print(key, value)

# Copy a dictionary
mydict_copy = mydict
print(mydict_copy)

## If this method is used, modifications on the copy are reflected in the 
## original
mydict_copy["email"] = "max@xyz.com"
print(mydict_copy)
print(mydict)

## The copy function can be used to avoid this
mydict.pop("email")
print(mydict)

mydict_copy = mydict.copy()
mydict_copy["email"] = "max@xyz.com"
print(mydict_copy)
print(mydict)

## Alternatively, we can use the dict function to make the copy
mydict_copy = dict(mydict)
mydict_copy["email"] = "max@xyz.com"
print(mydict_copy)
print(mydict)

# Update a dictionary based on another
mydict = {"name": "Max", "age": 28, "email": "max@xyz.com"}
mydict2 = dict(name = "Mary", age = 27, city = "Boston")
print(mydict)
print(mydict2)

mydict.update(mydict2)
print(mydict)

# Any inmutable type can be used as a key
## We can use numbers
mydict = {3: 9, 6: 36, 9: 81}
print(mydict)

## Using numbers as keys has the problem tha tsubsetign cannot be done using
## indexes as usual. We need to use the actual key number.
value = mydict[3]
print(value)

value = mydict[6]
print(value)

## Using tuples
mytuple = (8, 7)
mydict = {mytuple: 15}
print(mydict)

## Lists cannot be used, an error would be returned, because they are mutable
