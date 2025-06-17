# Accessing data from objects
class User:
  def __init__(self, username, email, password):
    self.username = username
    self.email = email
    self.password = password
  
  # We can define methods that receive data from a froeign object
  def say_hi_to_user(self, user):
    print(f"Sending meesage to {user.username}: Hi {user.username}, it's {self.username}")
  
user1 = User("dantheman", "dan@gmail.com", "123")
user2 = User("batman", "bat@outlook.com", "abc")

## Access email from user1
print(user1.email)

## user1 greets user2, using the method say_hi_to_user, which access the data
## from another user object
user1.say_hi_to_user(user2)

# We can modify the data in an object
print(user1.email)
user1.email = "danny@gmail.com"
print(user1.email)

## The problem here is that the value could be replaced with a non-valid value.
## We could provide a value that does not correspond to an email address.

## The traditional way to avoid this issue is to make the data private and use 
## getters and setters
class User:
  def __init__(self, username, email, password):
    self.username = username
    # Prefixing the attribute with "_" makes it protected
    # Meaning that the attribute should not be read outside of its corresponding
    # class
    self._email = email
    self.password = password
  
  def get_email(self):
    return self._email
  
  def clean_email(self):
    # The method returns an email in lower case and without whitespace around it
    return self._email.lower().strip()

user1 = User("dantheman", " Dan@gmail.com", "123")
user2 = User("batman", "Bat@outlook.com", "abc")

### A problem here is that by default python does not make a protected attribute 
### innaccessible from outside the class
print(user1._email)
### However, by convention we are not supposed to access values of a protected
### attribute from outside the class.
### Instead, we are supposed to use a method defined within the object class
print(user1.get_email())
print(user1.clean_email())
### Using this traditional approach we communicate to developers to not access,
### nor modify, the attribute from outside the class, and prevent that a 
### non-valid vlaue is given to it

### We can properly enforce the protection of an attribute by making it 
### private
class User:
  def __init__(self, username, email, password):
    self.username = username
    # Prefixing the attribute with "__" makes it private
    # Now, the attribute cannot be read outside of its corresponding class
    self.__email = email
    self.password = password
  
  def get_email(self):
    return self.__email
  
  def clean_email(self):
    # The method returns an email in lower case and without whitespace around it
    return self.__email.lower().strip()

user1 = User("dantheman", " Dan@gmail.com", "123")

### The following code will display an error, as the attibute's value cannot be 
### accessed outside of its class
"""
user1.__email
"""
### We have to use a method defined within the class
print(user1.get_email())
print(user1.clean_email())

### However, attributes should nto be made private unless absolutely necessary.
### Although python does nto enforce the protection of protected attributes, the
### convention communicates to developers that they should not access their
### values outside of the class
### So, get and set methods are needed.
### They provide full control on what happens when the value of an attribute
### is read or modified
from datetime import datetime

class User:
  def __init__(self, username, email, password):
    self.username = username
    self._email = email
    self.password = password
  
  # Get method
  def get_email(self):
    print(f"Email accessed at {datetime.now()}")
    return self._email
  
  #Set method
  def set_email(self, new_email):
    if "@" in new_email:
      self._email = new_email
    else:
      print("Provided email is not a valid email address")

user1 = User("dantheman", "dan@gmail.com", "123")
print(user1.get_email())
user1.set_email("dannygmail.com")
print(user1.get_email())
user1.set_email("danny@gmail.com")
print(user1.get_email())

## Another approach, and the recommended one, is to create getter and setter
## properties.
class User:
  def __init__(self, username, email, password):
    self.username = username
    # WE set the attribute as protected
    self._email = email
    self.password = password
    
  
  # getter property
  @property
  def email(self):
    print(f"Email accessed at {datetime.now()}")
    return self._email
  
  # setter property
  @email.setter
  def email(self, new_email):
    if "@" in new_email:
      print(f"Email modified at {datetime.now()}")
      self._email = new_email
    else:
      print("Provided email is not a valid email address")

user1 = User("dantheman", "dan@gmail.com", "123")
### Now we can access the email attribute, without accessing the protected 
### attribute directly.
### This allows to access the value with typical code (no need to think on 
### getter and setter methods in the code working with the object), while having
### full control of what happens when the values are accessed
print(user1.email)
user1.email = "This is not an email"
print(user1.email)
user1.email = "danny@outlook.com"
print(user1.email)
