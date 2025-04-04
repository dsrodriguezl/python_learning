# A dictionary is a special structure that allows storing information in
# key-value pairs. The values are associated to a key that can be used to access
# the specific value
monthConversions = {
  "Jan": "January",
  "Feb": "February",
  "Mar": "March",
  "Apr": "April",
  "May": "May",
  "Jun": "June",
  "Jul": "July",
  "Aug": "August",
  "Sep": "September",
  "Oct": "October",
  "Nov": "November",
  "Dec": "December",
}

# To access the values, we refer to the key within the dictionary
print(monthConversions["Jan"])
print(monthConversions.get("Dec"))

# If an unexisting key is specified, the code crashes if using []
# or returns "None" if using get
# A custom output can be also specified if using get
print(monthConversions.get("Luv", "Not a valid key"))
