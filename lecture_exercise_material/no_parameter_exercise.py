# function with no parameters exercise
# Do all of this in a .py file in Pycharm.
# Create a function called hello_world_printer() which takes no parameters and prints the string "hello world"
# Call the function hello_world_printer()
def hello_world_printer():
    print("hello world")


hello_world_printer()

#function with 1 parameter exercise :   Do all of this in a .py file in Pycharm
# Create a function called name_printer which takes 1 parameter and prints it
# Create a variable called name and assign it user input().  input()'s message should ask the user to enter their name.
# Call name_printer() with the variable "name" as its argument.
def name_printer(name):
    name = input(" Enter user name to Print : ")
    print(name)


name_printer('name')