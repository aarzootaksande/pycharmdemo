# dictionary methods 1 exercises; Do all of this in a .py file in Pycharm.
# 1. create a variable and assign it the
# following dictionary: a:  1 | {"Queen": "Bohemian Rhapsody", "Bee Gees": "Stayin' Alive", "U2": "One",
# "Michael Jackson": "Billie Jean", "The Beatles": "Hey Jude", "Bob Dylan": "Like A Rolling Stone"}
# 2. make the dictionary span multiple lines so that the line the dictionary starts on is not too long.

famous_songs = {"Queen": "Bohemian Rhapsody",
                "Bee Gees": "Stayin' Alive",
                "U2": "One",
                "Michael Jackson": "Billie Jean",
                "The Beatles": "Hey Jude",
                "Bob Dylan": "Like A Rolling Stone"}

# 3. print the length of the dictionary.
print(len(famous_songs))
# 4. use the .keys() method and a for loop to get and print all of the keys from the dictionary on separate lines.
for key in famous_songs.keys():
    print(key)
# 5. print all of the values from the dictionary using the .values() method.
for value in famous_songs.values():
    print(value)
# 6. use .items() with a for loop to iterate through and print all of the key value pairs from the dictionary.
for key, value in famous_songs.items():
    print(key, value)
# 7. use the .get() method to check the dictionary for the key
# a: 1 | "Promise of the Real"
# and create a message that will print if the key is not found in the dictionary.
print(famous_songs.get("Promise of the Real", "key is not found in the dictionary."))