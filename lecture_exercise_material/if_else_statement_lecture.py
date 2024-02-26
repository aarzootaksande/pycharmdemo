veg = input("Type the name of a vegetable. ")
# if statement
if veg == "corn":
    print("The Vegetable is corn. ")
else:  # else statement
    print("The Vegetable is not corn")

# nested if else statements
gpa = float(input("What was the applicant's grade point average ? "))
inst_app = input("Is the student going to be educated at an approved institution ")

if gpa >= 3.7:
    if inst_app == "yes":
        print("The application qualifies for a low APR student loan.")
    else:
        print("The application does not qualify since they have not been accepted into an approves institution. ")
else:
    print("The application did not have high enough grades to qualify.")