# Static attributes (also called class attributes) are attributes that belong
# to the class itself, not to a specific instance (object) of the class.
# So, they are shared among all instances of a class.

class User:
  # Static attributes
  user_count = 0
  
  # Instance attributes
  def __init__(self, user_name, email):
    self.username = user_name
    self.email = email
    # user_count is modified everytime a user is created
    # So, every user contains the number of total users
    User.user_count += 1
    
  def display_user(self):
    print(f"Username: {self.username}, Email: {self.email}")

user1 = User("dantheman", "dan@gmail.com")
user2 = User("sally123", "sally@gmail.com")

# We can access static attributes from the class and from each instance of it
print(User.user_count)
user1.display_user()
print(user1.user_count)
user2.display_user()
print(user2.user_count)

# Static vs. Instance method
class BankAccount:
  min_balance = 100
  
  def __init__(self, owner, balance = 0):
    self.owner = owner
    self._balance = balance
  
  # Instance method
  def deposit(self, amount):
    if amount > 0:
      self._balance += amount
      print(f"{self.owner}'s new balance: ${self._balance}")
    else:
      print("Deposit must be positive")
  
  # Static method
  @staticmethod
  def is_valid_interest_rate(rate):
    return 0 <= rate <= 5

account = BankAccount("Alice", 500)
account.deposit(200)

# Static methods do not exist on the instances, only in the class itself.
# So, they can only be accessed from the class
print(BankAccount.is_valid_interest_rate(3))
print(BankAccount.is_valid_interest_rate(10))
