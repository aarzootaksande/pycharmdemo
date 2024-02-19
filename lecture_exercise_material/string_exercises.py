# Strings Exercises
# Do all of this in a .py file in Pycharm
# Create a variable and assign it the string "Just do it!"
variable = "Just do it!"
str_variable = variable
print(str_variable)

# Access the "!" from the variable by index and print() it
print(str_variable[10:])
# Print the slice "do" from the variable
print(str_variable[4:7])
# Get and print the slice "it!" from the variable
print(str_variable[8:])
# Print the slice "Just" from the variable
print(str_variable[:4])
# Get the string slice "do it!" from the variable and concatenate it with the string "Don't ".
concatenated = "Don't"
# Print the resulting string, which should be "Don't do it!" where the "do it!" part is a slice.
print(concatenated + " " + (str_variable[5:11]))