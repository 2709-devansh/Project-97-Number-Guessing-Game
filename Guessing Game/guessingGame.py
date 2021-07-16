import random
number = random.randint(1,9)
chances = 0

print("NUMBER GUESSING GAME")
print("")
print("The computer selects a random number between 1 and 9, but it does not tell you which number it is. You will have 5 guesses in which you have to enter a number between 1 and 9, if the guess is correct then you win but if you do not guess the number in 5 chances you will lose the game!")
print("")

while chances < 5:    
    numberGuess = int(input("Enter Your Guess:"))

    if numberGuess == number:
        print("Excellent!, You guessed the Number")
        break

    elif numberGuess < number:
        print("Oh! Your guess was too low, try a larger number")
        print("")
        chances = chances + 1

    else:
        print("Oh!, Your guess was too large, try a smaller number")
        print("")
        chances = chances + 1

if not chances < 5:
    print("Sorry, You Lost, Better Luck next Time. The Number is ", number)


