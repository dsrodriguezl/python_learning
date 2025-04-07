from chef import chef

my_chef = chef()

my_chef.make_chicken()

# We can create a new class based on another, so it inherits all its attributes
# and functions
class chinese_chef(chef):
  # We cna also redefine attributes of the original object class and/or add new
  # ones
  def make_special_dish(self):
    print("The chef makes orange chicken")
  
  def make_fried_rice(self):
    print("The chef makes fried rice")

my_chinese_chef = chinese_chef()

my_chinese_chef.make_chicken()
my_chef.make_special_dish()
my_chinese_chef.make_special_dish()

