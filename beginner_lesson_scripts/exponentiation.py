
# It is easy to use exponentiation in python
print(2**3)

# How would we creae a function that performs this with a for loop?
def raise_to_power(base_num, pow_num):
  result = 1
  for index in range(pow_num):
    result = result * base_num
  return result

print(raise_to_power(2, 3))
