# Programming Challenge: Sum of Numbers From A Positive Integer
# Write a program which gets a positive integer from a user using input() and assigns it to a variable.
# The program should then use a while loop to get the sum of all the integers from the integer that was entered by
# the user down to 1. For example, if the integer entered by the user was 6, the while loop would find the sum of 6,
# 5, 4, 3, 2, and 1, which is 21.
# At the bottom of your program create two print statements.
# One will display the user entered integer and the other will display the sum found by the while loop.
positive_integer = input(" Enter a positive integer ")
print(" the user entered integer " + str(positive_integer))


sum = 0
while int(positive_integer) != 0:
    sum = sum + int(positive_integer)
    positive_integer = int(positive_integer) - 1


print(" Current Value of User entered Positive Integer is : " + str(positive_integer))
print("total sum is " + str(sum))