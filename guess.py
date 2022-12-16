#Homework
#Write a guessing game until the user gets it right.
#What is my favourite color
# If wrong, "Sorry please try again"
# If right, " Thanks its right" and exit
#loop, if conditions and print statements
import random
score = 0
colors = ["red", "silver","orange"]
chances = 10
print("You get 10 chances in this game and count down 10-zero")
while chances > 0:
    guess = input("Chance: " + str(chances) + " What is my favourite color ? ")
    print("Score is " + str(score))
    if guess.lower() == colors[random.randint(0, 2)]:
        print("Wow you guessed it right. Hurray!!")
        score = score + 1
        print("Score is " + str(score))
        if score ==5:
            print("You are a winner!! ")
            break
    else:
        # correct the logic here
        if score < 5 and chances < 2 :
            print("YOU LOST!!! ")
            print("Score is " + str(score))
        else:
            print("Sorry please try again!")
    chances = chances - 1
