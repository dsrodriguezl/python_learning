# Encapsulation
# It involves bundling the data, attribute, fields and methods, or behaviors
# that operate on the data into a single unit called a class.
# It helps in hidding the internal implementation details of a class by only 
# exposing the necessary fucntionalities to the outside world.

## No encapsulation example (what not to do)
class BadBankAccount:
  def __init__(self, balance):
    self.balance = balance

account = BadBankAccount(0.0)
account.balance = -1
## The prvious example hads the problem that it allows setting a negative (<0)
## account balance
print(account.balance)

## Better bank account example with encapsiulation of the filelds and internal 
## logic.
class BankAccount:
  def __init__(self):
    self._balance = 0.0
  
  @property
  def balance(self):
    return self._balance
  
  def deposit(self, amount):
    if amount <= 0:
      raise ValueError("Deposit amount must be positive")
    self._balance += amount
  
  def withdraw(self, amount):
    if amount <= 0:
      raise ValueError("Withdraw amount must be positive")
    if amount > self._balance:
      raise ValueError("Insufficient funds")
    self._balance -= amount

account = BankAccount()
print(account.balance)
## Now we cannot assign the account's balance a negative number
"""
# This code will display an error:
account.balance = -1

# Error in py_run_file_impl(file, local, convert) : 
#   AttributeError: property 'balance' of 'BankAccount' object has no setter
"""
account.deposit(1.99)
print(account.balance)
account.withdraw(1)
print(account.balance)
## We also cannot withdraw more than what the accoutn holds
"""
# This code will display an error:
account.withdraw(100)

# Error in py_run_file_impl(file, local, convert) : 
#   ValueError: Insufficient funds
"""
