# introduction to tuples : tuples are the datatypes made up of a collection of items
# they are enclosed in {}
tuple_1 = ("a", "b", "c", "d", "e")
tuple_2 = (2.718, False, [1, 2, 3])
tuple_3 = (1, 1, 0, 0, 0)

tuple_5 = ([3.14, 2.205, 10])
tuple_6 = tuple("edcba")
print(tuple_5)
print(tuple_6)
tuple_7 = tuple({"a": 1, "b": 2, "c": 3})
print(tuple_7)
tuple_8 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(tuple_8[2])
print(tuple_8[:8])
print(tuple_8[2:7])
print(tuple_8[3:])

# immutability of tuples
tuple_9 = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
tuple_10 = ("Fall", "Winter", "Spring", "Summer")
tuple_11 = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
            "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
tuple_12 = (1, 3, 5)
list_1 = [1, 3, 5]
print(tuple_12.__sizeof__())
print(list_1.__sizeof__())

# tuple looping and step lecture
marjo_cities = ("Tokoyo", "London", "New York", "Shanghai", "Sydney")
print("iterate through tuple using for loop")
# iterate through tuple using for loop
for city in marjo_cities:
    print(city)

# iterate through tuple using while loop
print("iterate through tuple using while loop")
count = 0
while count < len(marjo_cities):
    print(marjo_cities[count])
    count += 1

print("we can also use count backwards through tuples")
backwards = len(marjo_cities) - 1
while backwards >= 0:
    print(marjo_cities[backwards])
    backwards -= 1

# tuple slicing with step
print(" tuple slicing with step ")
ints = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(ints[::3])  # stride length of 3
print(ints[1::2])  # evens only
print(ints[7::-1])  # backwards from 8
print(ints[8::-2])  # odds only backwards

# tuple methods
# .nested()
print("  tuple methods : .nested()")
nested = (1, 2, 3, (4, 5, 6), (7, 8, 9), (10, 11, 12))
print(nested[4])
print(nested[5][1])
# .repeat() method
print(" for tuple method : .repeat() ")
repeat = (7, 3, 3, 3, 0, 0, 7, 0, 0)
print(repeat.count(7))
print(repeat.count(3))
print(repeat.count(0))

# .index() method
print(" for tuple method : .index() ")
ints = (1, 1, 7)
print(ints.index(7))
print(ints.index(1))