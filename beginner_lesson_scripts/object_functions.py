from student import student

student1 = student("Oscar", "Accounting", 3.1)
student2 = student("Phyllis", "Business", 3.8)

print("Is " + student1.name + " in honor roll?")
print(student1.on_honor_roll())
print("")
print("Is " + student2.name + " in honor roll?")
print(student2.on_honor_roll())
