# indexes and list slicing 4th March 2024
# accessing by index

indexes_example = ["carpet", "hardwood", "lionleum"]
print(indexes_example[2])

indexes_example2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(indexes_example2[2][1])
print(" ")
# negative indexes
negative = [1, 2, 3, 4, 5]
print(negative[-1])
print(negative[-2])
print(negative[-3])
print(negative[-4])
print(negative[-5])

# using items accessed by index in expressions
print("using items accessed by index in expressions :")
mixed = [False, 365, 4.24, "this is a string"]
print(mixed[2] + 1.76)
print("I have used \"" + mixed[-1] + "\" as an example too many times.")

# list slicing
sliced = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("list slicing lecture : " + str(sliced))
print(sliced[:4])
print(sliced[3:8])
print(sliced[6:])

# reassigning items in a list
print("resigning a list's item ")
example = [2, 4, 6, 8, 0]
print(example)
example[4:7] = [7, 6, 5]
print(example)