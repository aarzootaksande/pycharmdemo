# 6th March 2024 : Dictionary Methods 2 :
# .formkeys(), .pop(), and .popitem()
# .fromkeys() : the from keys methods returns a disctionary using 2 values that is was givena argument
ex_1 = {}.fromkeys(["addr"], "1600 Pennsylvania Avenue Nw")
print(ex_1)

# .pop()
ex_2 = {"make": "Honda",
        "model": "civic",
        "year": 2016}
ex_2.pop("model")
print(ex_2)


ex_3 = {"name": "bob",
        "age": 38,
        "occupation": "accountant",
        "workspace": "H&R block"}
ex_3.popitem()
print(ex_3)