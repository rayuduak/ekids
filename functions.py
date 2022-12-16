#Math library
# Add, Subtract, Multiply, Divide

def addfunc(a,b):
    return a+b

def subfunc(a,b):
    return a-b

#multiply and sub as HW.

 #week start monday to sunday and its 1-7
def findDayOfWeek(weeknum):
    match weeknum:
        case 1: return "Monday"
        case 2: return "Tuesday"
        case 3: return "Wednesday"
        case 4: return "Thursday"
        case 5: return "Friday"
        case 6: return "Saturday"
        case 7: return "Sunday"
        case _: return "Not valid"

def welcome(name):
    print("Welcome to my program : " + name)


welcome(input("what is your name? "))
x = 10
y = 5
z = addfunc(x,y)
print("Sum of x and y is " + str(z))
print("Subtraction of x and y " + str(subfunc(x,y)))
print(findDayOfWeek(2))
print(findDayOfWeek(6))
print(findDayOfWeek(7))