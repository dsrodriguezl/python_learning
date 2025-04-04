# We can import code from another python script
# As the scripts are not directly in the workign directory, but in the 
# subdirectory "beginner_leson_scripts", we need to specify this subdirectory
# using "from". The script also has a long name, so we can use "as" to stablish
# the name of the object of the module and avoid having to constantly refer
# to the long name of the script
from beginner_lesson_scripts import modules_pip_useful_tools as useful_tools

# Now we can access the variables and functions defined in the 
# modules_pip_useful_tools script
print(useful_tools.roll_dice(10))

# We can also import external modules
# If the module of interest is not installed, we can just install it before 
# importing it using pip install 'library name' in the terminal
# Here we have already installed python-docx and can import it
import docx

# To uninstall a library we can use pip uninstall 'library name' in the terminal
