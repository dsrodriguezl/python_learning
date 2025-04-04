# Try except blocks allow error handling, by avoiding the code to stop with an
# error
# The following code will not break if a text input is provided, and will alert
# the user that they provided an invalid input
try:
  number = int(input("Enter a number: "))
  print(number)
except:
  print("Invalid input")

# The problem witht he previous example is that the except will catch any type 
# of error in teh code, not only errors that are due to invalid user inputs
# Like with the code below, it stops because of the error of dividing by 0, but
# will still show the "Invalid input" message
try:
  value = 10 / 0
  number = int(input("Enter a number: "))
  print(number)
except:
  print("Invalid input")

# To correct this, we need to define the except differently, more specifically
try:
  value = 10 / 0
  number = int(input("Enter a number: "))
  print(number)
except ZeroDivisionError:
  print("Dividing by zero")
except ValueError:
  print("Invalid input")

