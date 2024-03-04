# del and list methods

planets = ["pluto", "mars", "earth", "venus"]
# del statements : to delete a entity from the list
del planets[0]
print(planets)

# remove statements : to remove any entry from the list which is passed as an argument
planets.remove("mars")
print(planets)

colors = ["blue", "red", "white", "blue", "orange", "blue"]
colors.remove("blue")  # only removes the first instance of blue from the list.
print("Print the colors list after removing blue as per the above line : " + str(colors))

# append statements : appends new entity in the list which is passed as an argument
planets.append("pluto")
print(planets)
# append adds somthing at the end of the list.
pets = ["cat", "dog", "parrot"]
print(pets)
pets.append("fish")
print(pets)

# insert statements : insert allows you to add an item any where in the list.
pets.insert(1, "turtle")
print(pets)

# sort statements : it sorts items for least to greatest
num_list = [2.718, 4, -19, 10000, 0]
print(num_list)
num_list.sort(reverse=True)
print(num_list)

str_list = ["Ringo", "John", "George", "Paul"]
print(str_list)
str_list.sort()  # sort sotrs the list alphabetically
print(str_list)

# sort does not workd on mixed list
# because python does not know how to sort between list with multiple data types
# mixed = [False, 5.67, "string", -2]
# mixed.sort()
# print(mixed)

# ASCIIbetiacal order and alphebetical order
print("sort method dosent actually uses alphebetical orders it actually uses ASCIIbetical order")
print("ASCIIbetical Order and Alphebetical orders are the same except in "
      "ASCIIbetiacal Order the Upper Case letters comes first and "
      "then the lower case letters")
ASCIIbetical = ["Andy", "kiwi", "apple", "Karen", "Brian", "banana"]
ASCIIbetical.sort(key=str.lower)
print(ASCIIbetical)

# .index
metals = ["copper", "gold", "silver", "iron"]
print(metals.index("silver"))

numbers = [4, 3, 2, 1, 0, 1, 2, 3, 4]
print(numbers.index(1))

# .pop()
# the pop methos removes and returns an item from the list
bands = ["Queen", "Led Zepplin", "The Beatles", "MUSE", "Radiohead"]
end = bands.pop(2)
print(bands)
print(end)