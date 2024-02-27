students_score = int(input(" Enter the score of the Student. "))

if students_score >= 90:
    print("This Students Score is : "+str(students_score)+" A score of 90 or above is an A grade. ")
else:
    if students_score >= 80:
        print("This Students Score is : "+str(students_score)+" A score of 80 or above is a B grade. ")
    else:
        if students_score >= 70:
            print("This Students Score is : "+str(students_score)+" A score of 70 or above is a C grade. ")
        else:
            if students_score >= 60:
                print("This Students Score is : "+str(students_score)+" A score of 60 or above is a D grade. ")
            else:
                print("This Students Score is : "+str(students_score)+" A score any lower is an F grade. ")