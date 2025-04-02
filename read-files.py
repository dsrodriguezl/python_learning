# open allows us to open fiels with python, the argument r specifies that we
# will only read the file
employee_file = open("employees.txt", "r")

# Is the file content readable?
print(employee_file.readable())

# Ensure to close the files you have opened
employee_file.close()

# We can read the entire file
employee_file = open("employees.txt", "r")
print(employee_file.read())
employee_file.close()

# readline access a line from the file. Each call of the fucntion reads the line
# after the one that was read by the previous call.
employee_file = open("employees.txt", "r")
print(employee_file.readline())
print(employee_file.readline())
employee_file.close()

# readlines place all lines inteh file within a list
employee_file = open("employees.txt", "r")
employees = employee_file.readlines()
print(employees)
# We can access specific lines by referring to their indes within the list
print(employees[0])
print(employees[1])

for employee in employees:
  print(employee)

employee_file.close()
