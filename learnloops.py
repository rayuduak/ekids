#Sesion 3 - Loops
print("this is lesson for learning loops")
#for
#while

countries = ["Portugal", "Swis", "Morocco", "Spain", "Brazil", "Japan"]
i =1
#This is for loop syntax.
for name in countries:
    print("{} {}".format(i , name))
    i = i+1

phrase = "Hello My name is rayudu , My students are Tim and Aorahee"
splitarray = phrase.split()
print(type(splitarray))
for word in splitarray:
    if word == "students":
        print(word)

#while loop.
countofwords = len(splitarray)
i = 1
while i < countofwords:
    print(splitarray[i])
    i = i+1

colors = "this string has many colors red green blue yellow and many others, blue and blue and blue i have red again"
splitwords = colors.split()
#print(type(splitwords))
red = 0
green = 0
blue = 0
yellow = 0
for word in splitwords:
    if word == "red":
        red = red + 1
    elif word == "blue":
        blue = blue + 1

print("red : " + str(red))
print("blue: " + str(blue))


