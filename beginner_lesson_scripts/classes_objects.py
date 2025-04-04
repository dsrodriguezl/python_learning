# We can create our own data types
class student:
  # We need an initialize function to define the attributes of this class
  def __init__(self, name, major, gpa, is_on_probation):
    # We define the indexing labels for each of the attribute values within the 
    # object
    self.name = name
    self.major = major
    self.gpa = gpa
    self.is_on_probation = is_on_probation


# Let's use our newly created class
student1 = student("Jim", "Business", 3.1, False)
student2 = student("Pam", "Art", 2.5, True)

print(student1.name)
print(student2.gpa)
