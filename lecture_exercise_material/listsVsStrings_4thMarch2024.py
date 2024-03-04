# Lists and String both contains an ordered sequence of items
# several thoins that can be done with lists can also be done with strings
# both have indexe numbers correcponding to what they contains
# for loop and while loop can be used to operate on lists and strings
# Difference in list and String
# Lists = mutable   :  we can uses slicsed and replace items in this
# Strings = immutable : but in string we cannot change replace itmes in strings.
# -----------------------

# list example : lists are mutable
ex_1 = [1, 2, 3]
ex_1[1] = 5
print(ex_1)

# string assign to a variable to demo strings are immutable
# gives error : TypeError: 'str' object does not support item assignment

ex_2 = "123"  # strings items are immutable
# ex_21 = "153"  # in orders to change one thing from the string we have to reassign entir string
# print(ex_21)

# best practice is creating new String using old string using concatenation
ex_9 = [1, 2, 3, 4, 5]
ex_10 = ex_9
ex_10[2] = 4
print(ex_9)
print(ex_10)

# copy module and deepcopy()  we need to import copy module
import copy

ex_12 = [1, 2, 3, 4, 5]
ex_13 = copy.deepcopy(ex_12)


ex_15 = [ "bush",
          "fern",
          "tree",
          "moss"]
print(ex_15)

# \ line continuation
print("line continuation lecture ")
ex_16 = 2 + \
        4 + \
        1
print(ex_16)

ex_18 = ("hello" + \
         "world")

print(ex_18)