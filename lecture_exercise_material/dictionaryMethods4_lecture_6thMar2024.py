# dictionary methods 4 lecture method .setdefault()
computers = {"Google": "ChromeBook",
             "Apple": "MacBook",
             "Microsoft": "Surface Pro"}
if "Lenovo" not in computers:
    computers["Lenovo"] = "ThinkPad"

print(computers)

# if we wanted to use setdefault

computers.setdefault("Lenovo", "IdeaPad")
print(computers)