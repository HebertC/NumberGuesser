__author__ = 'casey'

import random

def main():
    #Guess Counter
    counter = 1 # counts the one correct one
    #varibles
   #pick a number
    print("Choose a range of numbers to guess from")
    low_number = int(input("First, choose the lowest number in range: "))
    high_number = int(input("Second, choose the highest number in range: "))
    print("I've picked a number.")

    randNumber = random.randint(low_number, high_number)

    while True:
        #pick a number

        guessedNumber = int(input("Guess what it is: "))


        if guessedNumber == randNumber:
            print(guessedNumber)
            print("That's correct! How did you know??")
            print("Guess attempts  -> " + str(counter))
            break

        elif guessedNumber < randNumber:
            print(guessedNumber)
            print("Too low. Try again")
            counter +=1

        elif guessedNumber > randNumber:
            print(guessedNumber)
            print("Too high. Try again")
            counter +=1
main()

