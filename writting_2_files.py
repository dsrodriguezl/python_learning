employee_file = open("employees.txt", "r")
print(employee_file.read())
employee_file.close()

# We can use open with the argument a to append information to a file
employee_file = open("employees.txt", "a")
# We write in the end of the file the information of another employee
employee_file.write("Toby - Human Resources")
employee_file.close()

employee_file = open("employees.txt", "r")
print(employee_file.read())
employee_file.close()

# What if we re-run the code to append the same information to the file?
# We can use open with the argument a to append information to a file
employee_file = open("employees.txt", "a")
employee_file.write("Toby - Human Resources")
employee_file.close()

employee_file = open("employees.txt", "r")
print(employee_file.read())
employee_file.close()
# This time the information was added ont he same line, because the file did not
# end with a line break. To avoid this we can use the \n special character, 
# which inserts a line break
employee_file = open("employees.txt", "a")
employee_file.write("\nKelly - Customer Service")
employee_file.close()

employee_file = open("employees.txt", "r")
print(employee_file.read())
employee_file.close()

# What if we just want to write a file instead of appending to it?
employee_file = open("employees.txt", "w")
employee_file.write("Jim - Salesman\nDwight - Salesman\nPam - Receptionist\nMichael - Manager\nOscar - Accountant")
employee_file.close()

# Using open with the w argument, writting mode, will overwrite the whole 
# content of the file.
# It can also be used to write a new file
employee_file = open("employees1.txt", "w")
employee_file.write("Kelly - Customer Service")
employee_file.close()

# We can also create other type of files, not just .TXT
employee_file = open("employees1.html", "w")
employee_file.write("<p>Kelly - Customer Service</p>")
employee_file.close()
