# input () function is used to accept input from the user
name = input("Please enter your name.")
print("Your name is " + name + ".")
print(type(name))

fav_num = input("What is your favorite number ? ")
print("Your favorite number is " + fav_num + ".")
print(type(fav_num))

# Programming Challenge: Monty Python
# In a .py file, create a program and use input() three times to get answers to the following questions from a user.  Store each of the answers in a variable.
# What is your name?
name = input("What is your name ?")
# What is your quest?
quest = input("What is your quest ?")
# What is your favorite color?
fav_color = input("What is your color ?")
# Then, concatenate everything into a string within a print() statement with the form "So your name is [name], your quest is [quest], and your favorite color is [color]."
print("So your name is " + name + "," + "your quest is " + quest + "," + "and your favorite color is " +fav_color + ".")