 # As with attributes, we can make methods public, protected, or private to 
 # control access
class BankAccount:
  min_balance = 100
   
  def __init__(self, owner, balance = 0):
   self.owner = owner
   self._balance = balance
   
  # Public method accessing protected and private methods
  def deposit(self, amount):
   if self._is_valid_amount(amount) :
     self._balance += amount
     self.__log_transaction("deposit", amount)
   else:
     print("Deposit must be positive")
   
  # protected method
  def _is_valid_amount(self, amount):
   return amount > 0
 
  # private method
  def __log_transaction(self, transaction_type, amount):
   print(f"Logging {transaction_type} of ${amount}. New balance: ${self._balance}")

  @staticmethod
  def is_valid_interest_rate(rate):
   return 0 <= rate <= 5

account = BankAccount("Alice", 500)
account.deposit(200)

# Remeber that although we can access protected methods outside of the class,
# we should not
account._is_valid_amount(200) # This should not be done

# Private methods cannot be accessed outside the class
"""
# This code produces an error if run
account.__log_transaction("deposit", 200)
"""
