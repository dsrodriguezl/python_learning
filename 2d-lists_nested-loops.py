
# Lists can contain other lists
number_grid = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0]
]

# We can access the values using their indexes [row][column]
print(number_grid[0][0])
print(number_grid[0][1])
print(number_grid[1][0])
print(number_grid[3][0])


# For loops can be nested
# For example here we nested two for loops to access all the individual values 
# in the numbre_grid 2D (nested) list
for row in number_grid:
  for column in row:
    print(column)
