# This time we will make a calculator that will be able to perform all the 
# basic arithmetic calculations +, -, *, and /
# float transforms its input, a strign holding a number, into a nummeric 
# variable
num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
  print(num1 + num2)
elif op == "-":
  print(num1 - num2)
elif op == "/":
  print(num1 / num2)
elif op == "*":
  print(num1 * num2)
else:
  print("Invalid operator")
