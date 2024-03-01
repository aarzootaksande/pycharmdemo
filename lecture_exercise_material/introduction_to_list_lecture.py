# Introduction to lists : list is a datatype which contains multiple values in an ordered sequence
example_list_1 = [5, 4, 3, 2, 1]
example_list_2 = [2.5, 3.04, 2.503, 2.5, 1.42]
example_list_3 = ["blue", "green", "red", "yellow", "purple", "orange"]
example_list_4 = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]   # list of list

print(list("blah"))

# in and not in operator are used to check values present in or not present in list
checked_list = [1, 2, 3, 4]
print(1 in checked_list)
print(5 in checked_list)

not_in_example = 8 not in checked_list
print(not_in_example)