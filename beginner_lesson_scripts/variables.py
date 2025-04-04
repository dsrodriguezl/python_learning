
# The following code prints a short story
print("There once was a man named Gerorge, ")
print("he was 70 years old.")
print("He really liked the name George, ")
print("but didn't like being 70.")

# If we would like to change the name of theman int he story, we would normally
# have to change it manually in each print execution.
# To do this with a small program like the one above is not so difficult,
# although tedious.
# With bigger programs, this could be a very complicated task.
# Using variables simplify the job, ensuring reliability.

# Define variables
character_name = "John"
character_age = "35"

# Now we can use the variables in other code executions within this program

# Using + within the print execution concatenates entries without spaces 
# between them
print("There once was a man named " + character_name + ",")
# Using , within the print execution concatenates entries with spaces 
# between them
print("he was", character_age,"years old.")
#These methods can be combined within a print execution
print("He really liked the name", character_name +",")
print("but didn't like being",character_age + ".")

# We can update variables' values at any time
print("There once was a man named " + character_name + ",")
print("he was", character_age,"years old.")
character_name = "Mike"
print("He really liked the name", character_name +",")
print("but didn't like being",character_age + ".")

# There is different data types that can be stored in a variable
# So far, we used string (text) variables.
# We can also store numbers.
# Such like integers
character_age = 35
# We cna also use number with decimals
character_age = 35.3

print("There once was a man named " + character_name + ",")
print("he was", character_age,"years old.")
print("He really liked the name", character_name +",")
# print cannot handle numbers with the + operator.
# A text cannot be mathematically added to a number.
print("but didn't like being", character_age, ".")

# Another variable type is booleans TRUE or FALSE, which can be very useful
# when coding.
is_male = False

