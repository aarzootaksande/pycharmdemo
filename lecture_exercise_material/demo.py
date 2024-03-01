print("Hello World")

# Variables Assignment
ex_var = 5
# Variables Reassignments
ex_var = 7

# Floating-Ponit Numbers
float_1 = 1.2345
float_2 = -1.25
float_3 = 0.0
float_4 = 13.0
float_5 = -0.5

# Integers
int_1 = 7
int_2 = -52
int_3 = 0
int_4 = 900
int_5 = -749


# The argument fac_num's name is short for factorial number.
def factorial(fac_num):
    # The local variable returned will be used in the for loop used to calculate fac_num's
    # factorial. To do this, it will be multiplied by decrementing values of
    # fac_num. Since it will be multiplied, it was given the initial value of 1.
    returned = 1
    # By the end of this for loop, returned will have been reassigned fac_num's factorial.
    for item in range(fac_num, 1, -1):
        returned *= item

    # returns returned, which now holds the value of fac_num's factorial
    return returned


print(factorial(3))  # 6
print(factorial(4))  # 24
print(factorial(5))  # 120