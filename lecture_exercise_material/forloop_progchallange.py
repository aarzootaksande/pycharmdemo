# Programming Challenge: Find The Number of Characters in A String
# In a .py file, write a program which calculates the number of characters in a string.
# The string should be entered using input() and assigned to a variable.
# Use print() twice at the end of your program.  The first print() will print the string that the user entered and the second print() will display the number of characters in the string.
# For example, if the user entered the string "hello world", the number of characters would be 11.
print("Programming Challenge: Find The Number of Characters in A String")
counter = 0
user_entered_string = input("Enter a string and assign to a variable. ")

for letter in user_entered_string:
    print(" : " + letter)
    counter += 1

print("The string that the user entered is : " + str(user_entered_string))
print("The number of Character " + str(counter))