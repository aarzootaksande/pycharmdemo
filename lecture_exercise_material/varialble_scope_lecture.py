import breakfast

example = "hello global world"  # global scope variable


def loc_ex():
    example = "hello local world "  # local scope variable
    return example


print(example)
print(loc_ex())


# Local variable cannot be used by code in the global scope.
def loc_example():
    breakfast = "waffles"
    return breakfast


print("Local variable cannot be used by code in the global scope.")
loc_example()
print(breakfast)


# Global variables can be accessed by code in a local scope
def print_glob():
    print(glob_var)


glob_var = "This is a String for glob_var"
print_glob()