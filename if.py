# If statements are used for conditional execution of code
is_male = True

if is_male:
  print("You are a male")

is_male = False
if is_male:
  print("You are a male")

# else can be used for more complex if statements including the otherwise case
is_male = False
if is_male:
  print("You are a male")
else:
  print("You are not a male")

# or & and operators can be used within if statements for complex operations
is_male = True
is_tall = True

if is_male or is_tall:
  print("You are male or tall or both")
else:
  print("You are not male nor tall")

if is_male and is_tall:
  print("You are male and tall")
else:
  print("You are either not male or not tall or both")

# elif can be used for else if statements
# not allows more complex options
is_tall = False
if is_male and is_tall:
  print("You are male and tall")
elif is_male and not(is_tall):
  print("You are a short male")
elif not(is_male) and is_tall:
  print("You are not a male but tall")
else:
  print("You are either not male and not tall")

is_male = False
if is_male and is_tall:
  print("You are male and tall")
elif is_male and not(is_tall):
  print("You are a short male")
elif not(is_male) and is_tall:
  print("You are not a male but tall")
else:
  print("You are not male and not tall")

# if statements can be used for comparisons
# For comparisons we need to use the <, >, <=, >=, !=, and == operators
def max_num(num1, num2, num3):
  # If num1 is greater or equal than num2 and num3
  if num1 >= num2 and num1 >= num3:
    return num1
  # If num2 is greater or equal than the other two
  elif num2 >= num1 and num2 >= num3:
    return num2
  # If num1 and num2 aren't the biggest, num3 must be the biggest
  else:
    return num3

print(max_num(300,40,5))







