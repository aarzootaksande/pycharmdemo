# introduction to sets 6th march 2024
# a set is a datatype that consists fo collection of a item of much like a list
# however set differs from list in 2 ways : 1st they cannot have duplicate values
# 2nd the itme they contain are unordered

set_1 = {9, 8, 7, 6}  # set literal
set_2 = set({"a", "a", "b", "c", "d", "e"})  # duplicate items will be ignored
print(set_1)
print(set_2)

set_3 = set(range(1, 12, 2))
print(set_3)
# set can hold items that are of different datatypes
set_4 = {"a", 3.14, 18, True}
print(" set can hold items that are of different datatypes : ")
print(set_4)

# unlike lists , sets cannot have items accessed by index
set_5 = {3, 6, 9, 12, 15}
print (12 in set_5)
# for num in set_5:
# print(num)


# set methods
# .add()
scifi = {"star trek,"
         "star wars",
         "halo"}
scifi.add("mass effects")
print(scifi)

# .remove()
fruits = { "apple", "orange", "banana", "tomato"}
fruits.remove("tomato")
print(fruits)

# .discard()
fruits.discard("tomato")
print(fruits)

# .clear()
mountains = {"Everest", "Kilimanjaro", "Fuji"}
print(mountains)
mountains.clear()
print(mountains)

# .copy() method
mountains = {"Everest", "Kilimanjaro", "Fuji"}
set_2 = mountains.copy()
print(set_2)

# .union() method
set_1 = {1, 2, 3, 4, 5}
set_2 = {6, 7, 8, 9, 10}
set_3 = set_1.union(set_2)
# set_3 = set_1 | set_2
print(set_3)

# .intersection()

set_3 = set_1.intersection(set_2)
print(set_3)

# we can also use &  for intersection
set_3 = set_1 & set_2
print(set_3)

# substration and .difference()
set_11 = {1, 2, 3, 4, 5}
set_22 = {6, 7, 8, 9, 10}
set_33 = set_11.difference(set_22)
print(set_33)

# set comprehension
comp_1 = {even+2 for even in range(2, 11, 2)}
print(comp_1)

# set comprehension involving string
comp_2 = {char.lower() for char in "ALLCAPS"}
print(comp_2)