def function_name():
    print("This ")
    print("is ")
    print("an ")
    print("example ")


def function_sum(parameter):
    print(parameter+2)


first_str = "The number "
def function_multiple_parameter(p1, p2, p3):
    print(p1 + str(p2) + str(p3))


print("Calling the Defined Function Now")
function_name()

print("Calling Summ function : ")
function_sum(3)

function_multiple_parameter(first_str, 5, " is an integer.")


#defalut values to parameters

def function_defalut_values(num1=7, num2=8):
    print(num1*num2)
    return num1*num2

function_defalut_values(0, 3)
return_val = function_defalut_values(3, 3)
print(return_val)