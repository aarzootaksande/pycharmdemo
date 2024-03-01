# string method 2 .rjust() and .ljust() with one argument
print("hello world".rjust(4)+"----")
print("~~~~"+"hello world".ljust(15))

# with second argument in .rjust(arg1, arg2) and .ljust(arg1, arg2)
print("hello world".rjust(20, "*")+"==")

print("~~"+"hello world".ljust(20, "*"))

# with .center() with one argument and with two argument
print("hello world".center(20))
print("hello world".center(20, ":"))

# with methods only get operated on strings
# .strip(), .rstrip(), and .lstrip()
print("I had an exciting trip!!!11111")
print("I had an exciting trip!!!11111".strip("1"))
print("I had an exciting trip!!!11111".rstrip("1"))
print("I had an exciting trip!!!11111".lstrip("!"))

print("blueblueyellowblue".strip("uelb"))

print("juice, bread, cheese, beef, bread".rstrip(",bread"))
print("juice, bread, cheese, beef, bread".rstrip(",ed arb"))

print("juice, bread, cheese, beef, bread".lstrip(",juice"))
print("juice, bread, cheese, beef, bread".lstrip(",ju ce"))

# .replace(arg1, arg2)
print("Good morning".replace("Morning", "Afternoon"))