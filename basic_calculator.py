# Take the user input for both numbers and retunr the sum

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = num1 + num2
print(result)

# The previous code will concatenate the user inputs, as input automatically 
# transforms the input into a string

# The following transforms num1 and 2 into integers before summing them
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = int(num1) + int(num2)
print(result)

# If we want the calculator to be able to deal with decimals
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = float(num1) + float(num2)
print(result)
