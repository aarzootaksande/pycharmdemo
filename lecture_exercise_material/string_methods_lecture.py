# .upper() and .lower()
all_low = "these are no capitals here."
all_up = all_low.upper()
print(all_low.upper())
print(all_up)
print(str(all_up.lower()))
print("\n")
# .isupper() and .islower()

print("Mixed Case".isupper())
print("ALL CAPS !".isupper())

print("ALL CAPS!".islower())
print("all lower case".islower())

print("For Empty String")
print("".isupper())
print("String with special symbols and characters")
print("37&**&:\"".islower())
# For Multiple String Methods
print("For Multiple String Methods")
print("SHOUT!".lower().islower())

print("Batman".isalpha())
print("Batman123".isalnum())
print("123".isdecimal())
print("3.14".isdecimal())
print(" ".isspace())
print("            ".isspace())
print("not just spaces".isspace())
print("not just spaces"[3].isspace())
print("The Empire Strikes Back".istitle())
print("the great gatsby".title())

print("this is a string".startswith("this"))
print("To infinity and beyond!".endswith("beyond!"))

print("".join(["one", "two", "three"]))

print("Eggs, Milk, Waffles, Bacon".split(", "))