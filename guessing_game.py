import random

def userguess(x):
    randomnumber = random.randint(x, 100)
    uguess = 101  
    while uguess != randomnumber:
        uguess = int(input("Guess a number between " + str(x) + " and 100: "))
        if uguess < randomnumber:
            print("The number is higher")
        elif uguess > randomnumber:
            print("The number is lower")

    print("You guessed " + str(randomnumber) + ". That is correct!")

def compguesses(x):
    low = x
    high = 100
    response = " "
    while response != "c":
        if low != high: 
            compguess = random.randint(low, high)
        else:
            compguess = low
        response = input("Is " + str(compguess) + " too high (H), too low (L) or correct (C) ?").lower()
        if response == "h":
            high = compguess - 1
        elif response == "l":
            high = compguess + 1
    
    print(" The computer guessed your number. It was " + str(compguess) + ".")

which_game = input("What game would you like to play? (User guess, computer guess, or quit): ").lower()

if which_game == "user guess":
    print("The computer has chosen a number, and it is up to you to guess it. Enter your guess, and the computer will tell if the answer is higher or lower.")
    x = int(input("Enter a minimum whole number that is less than 100: "))
    userguess(x)
elif which_game == "computer guess":
    print("Pick a number between the range you have chosen, and the computer will try to guess what you are thinking.")
    x = int(input("Enter a minimum whole number that is less than 100: "))
    compguesses(x)
elif which_game == "quit":
    print("You have successfully quit.")
else:
    print("Invalid input. Click run and choose again.")
