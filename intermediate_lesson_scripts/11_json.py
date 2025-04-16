# Java Script Object Notation: Is a light weight data format that is used for 
# data exchange.
# Heavily used for web applications

import json

# python - JSON encoding/serialisation/conversion
person = {
  "name": "John",
  "age": 30,
  "city": "New York",
  "hasChildren": False, 
  "titles": ["engineer", "programmer"]
}

personJSON = json.dumps(person)

print(person)
print(personJSON)

## We can specify an indentation in the format
personJSON = json.dumps(person, indent = 4)
print(personJSON)

## We can specify different separators
## Note: It is recommended to stick to the default ones.
personJSON = json.dumps(person, indent = 4, separators = ("; ", " = "))
print(personJSON)

##  The sort_key argument can be helpful
personJSON = json.dumps(person, indent = 4, sort_keys = True)
print(personJSON)

with open("person.json", "w") as file:
  json.dump(person, file, indent = 4)

# deserialization/decoding
person = json.loads(personJSON)
print(person)

with open("person.json", "r") as file:
  person = json.load(file)

print(person)

# Working with custom objects
class User:
  
  def __init__(self, name, age):
    self.name = name
    self.age = age

user = User("Max", 27)

## We need to define a custom encoding function
def encode_user(o):
  if isinstance(o, User):
    return {"name": o.name, "age": o.age, o.__class__.__name__: True}
  else:
    raise TypeError("Object of type User is not JSON serializable")

### Now we pass the cutsom encoding function to the json.dumps function
userJSON = json.dumps(user, default = encode_user, indent = 4)
print(userJSON)

## We can also implement a custom JSON encoder
from json import JSONEncoder

class UserEncoder(JSONEncoder):
    
    def default(self, o):
      if isinstance(o, User):
        return {"name": o.name, "age": o.age, o.__class__.__name__: True}
      else:
        return JSONEncoder.default(self, o)

userJSON = json.dumps(user, cls = UserEncoder, indent = 4)
print(userJSON)

### We can use the UserEncoder directly
userJSON = UserEncoder(indent = 4).encode(user)
print(userJSON)


## deserialization

def decode_user(dct):
  if User.__name__ in dct:
    return User(name = dct["name"], age = dct["age"])
  else:
    return dct

user = json.loads(userJSON, object_hook = decode_user)
print(user)
print(type(user))
print(user.name)
