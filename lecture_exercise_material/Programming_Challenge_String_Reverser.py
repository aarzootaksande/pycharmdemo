# Programming Challenge: String Reverser
# For this challenge, you will be writing a program which uses a for loop to reverse a string.
# Start by creating a variable and assigning it a string as user input using input().
# Use a for loop to reverse the string.  You will need to use range with all 3 inputs for this.
# In addition, you should create a variable before the for loop and assign it an empty string.
# The variable will be reassigned multiple times within the for loop and end up holding the new reversed string.
#
# Print the reversed string at the bottom of your program.

user_string = input("Please enter a string.")
reversed = ""
print(len(user_string))
print(len(reversed))
for item in range(len(user_string) - 1, -1, -1):
    reversed += user_string[item]


print(len(reversed))
print(reversed)