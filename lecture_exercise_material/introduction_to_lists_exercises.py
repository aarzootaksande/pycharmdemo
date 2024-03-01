# introduction to lists exercises: Do all of this in a .py file in Pycharm.
# 1. Create a variable and assign it a list that contains an integer, a float, a Boolean value, a string, and a list of 3 integers.
var_list = [9, 8.32, 7, 6.201, True, "Arju qa", [3, 2, 1]]
print(list(var_list))
# 2. Create another variable and assign it a call of the list() function with a string as its argument.

li_str = list("cheese")
print(li_str)
print("e" in li_str)
# 3. Use the keyword "in" to check if the letter "e" is in the list assigned to the variable from step 2 and print the result.
print("a" in var_list)

# 4. Use the keyword "not in" to check if the letter "a" is not in the list assigned to the variable from step 2 and print the result.
print("a" not in li_str)
print("a" not in var_list)