# We can combine or stablish realtions between objects of custom classes
class Dog:
  def __init__(self, name, breed, owner):
    self.name = name
    self.breed = breed
    self.owner = owner
    
  def brak(self):
    print("Whoof whoof")
  
class Owner:
  def __init__(self, name, address, contact_number):
    self.name = name
    self.address = address
    self.phone_number = contact_number
  
owner1 = Owner("Danny", "122 Springfield Drive", "888-999")
dog1 = Dog("Bruce", "Yorkshire terrier", owner1)

print(owner1.name)
print(owner1.phone_number)
print(dog1.name)

print(dog1.name, "belongs to", dog1.owner.name)
