# Nov23 - strings
# playing with strings
fullname = "Joel Fedorenko"
name = fullname.split()
firstname = name[0]
lastname = name[1]
print(firstname)
print(lastname)
print(fullname)
print(fullname.upper())
print(fullname.lower())
print(fullname.replace('o','0'))


fname = ["Aarohe", "Tim"]
lname = ["Patel","TimLastname" ]
age = ["12", "11"]
city = ["Toronto", "Oakville"]

print("My name is {} {} and my age is {} and I am from {}".format(fname,lname, age, city))

# homework to print the 2 people details seperately
# you need to list index and how to get the right names. string format.

# Assume Tim went to TimHortons for buying a meal.
# He gets a milk, a cookie and sandwich for $1, $2, $5 respectively
# Homework: Create an array of items he bought and print
# Print the total amount he spent.
"""
Output:
Tim purchased these items from TimHortons and it cost him $8 Dollars
"""
a = "1234"
b = "John "
print(a.isdigit()) #return boolean, its give True or False
#if conditions
if a.isdigit() :
    print("a is a digit")
else:
    print("a is not a digit")

#weather
allowedWeather= ["sunny", "rain"]
#go play if weather is not snow or rain
todaysWeather = "snow"
#We need to check if todaysWeather is in the allowedWeather list above

#if todaysWeather is in notallowedWeather then "kid cannot play" elee 'he can play'
#comparision we need to use ==

if todaysWeather == allowedWeather[0] or todaysWeather == allowedWeather[1] :
    print("He can play play")
else:
    print("he cannot play")
