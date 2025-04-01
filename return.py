 # Return allows specifying what value a function should give as its output

# The following code returns "None"
def cube(num):
  num * num * num

print(cube(3))

# This version of the code should return the cube of the specified number
def cube(num):
  return num * num * num

print(cube(3))

result = cube(4)
print(result)

# return ends the function code, so any code indented into the function that
# is located after the return statement is not going to be executed when the 
# function is used
def cube(num):
  return num * num * num
  print("code")

print(cube(3))
