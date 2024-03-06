# dictionary method 3 : .clear(), copy(), and .update()
ex_1 = {1: "England",
        2: "Scotland",
        3: "Wales",
        4: "Northern Ireland"}
print(ex_1)
# .clear() method
ex_1.clear()
print(ex_1)

# .copy() method
birth_years = {1994: "bill",
               1969: "emily",
               1982: "elizabeth",
               2000: "turner"}
print(birth_years)
people = (birth_years).copy()
people[1982] = "madeline"
print(birth_years)

# .update() method
city_info = {"country": "canada",
             "province": "Ontario",
             "city": "Toranto"}
population = {"population": 2930000}
city_info.update(population)
city_info["population"] = 3000000
print(city_info)
city_info.update(population)
print(city_info)