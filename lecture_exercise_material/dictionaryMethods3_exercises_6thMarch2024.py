# dictionary methods 3 exercises
# Do all of this in a .py file in Pycharm.
#
# 1. paste these 2 dictionaries into your file
# a. 1 | internet_celebrities = {"DrDisrespect": "YouTube", "ZLaner": "Facebook", "Ninja": "Mixer"}
# b. 2 | another_one = {"shroud": "Twitch"}

internet_celebrities = {"DrDisrespect": "YouTube", "ZLaner": "Facebook", "Ninja": "Mixer"}
another_one = {"shroud": "Twitch"}

# 2. use .update() to add the contents of another_one to internet_celebrities.
internet_celebrities.update(another_one)
# 3. create a variable and assign it a copy of internet_celebrities.
gamers = internet_celebrities
# 4. use the .clear() method to get rid of the contents of internet celebrities.
internet_celebrities.clear()
# 5. print internet_celebrities.
print(internet_celebrities)
# 6. print the variable you created in step 3.
print(gamers)