# Programming Challenge: Factorial
# Create a function which takes one positive integer as its input and returns its factorial.
#
# To make sure that your function works correctly, you should call it with the inputs 3, 4, and 5 and print what is
# returned by those calls.  For those inputs, you should get 6, 24, and 120, respectively.

def factorial(fac_num):
    returned = 1
    for item in range(fac_num, 1, -1):
        returned *= item
    return returned

num1 = factorial(3)
print("Factorial for the number entered by user is :" + str(num1))
num2 = factorial(4)
print("Factorial for the number entered by user is :" + str(num2))
num3 = factorial(5)
print("Factorial for the number entered by user is :" + str(num3))