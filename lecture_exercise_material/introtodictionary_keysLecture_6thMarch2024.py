# .keys() method
birth_years = {1994: "bill",
               1969: "emily",
               1982: "elizabeth",
               2000: "turner"}
print(birth_years.keys())
for key in birth_years.keys():
    print(key)

# .values() method
print(birth_years.values())
for value in birth_years.values():
    print(value)

# .items() method on a dictionary python returns a list of tuples
# each of the tuples returns a key n its value
print(birth_years.items())
for key, value in birth_years.items():
    print(key, value)

print("------------")
print(type(birth_years.keys()))
print(type(birth_years.values()))
print(type(birth_years.items()))

# if you wanted to return a list of the above datatype use list function in place of type
print(list(birth_years.keys()))
print(list(birth_years.values()))
print(list(birth_years.items()))

# using in and not in on values : suppose if you wanted to check if a vule is present in a dictionary
print("elizabeth" in birth_years.values())
# .get() method allows us to look for and get key for a dictrionary
if 1975 in birth_years:
    print(birth_years[1975])
else:
    print("1975 is not a key in birth_years.")

print(birth_years.get(1975, "1975 is not a key in birth_years."))

# other things you should know about dictionaries dictionaries are mutable datatype like lists which means that
# variables which are assign to dictionaries also hold references to dictionaries not the dictionary values if a
# dictionary gets too long you can also make it expand into multiple lines
print(birth_years)
people = birth_years
people[1982] = "madeline"
print(birth_years)