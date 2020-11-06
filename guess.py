import random   #importing random library

secret_number = random.randrange(1,101)   #Set variable with range from 1 to 100

guess = 0  #set guess variable to 0
tries = 0  #set try variable to 0

#Set A while condition

while guess != secret_number:
    guess = int(input("Guess a number: "))
    print(guess)
    tries += 1

    if guess < secret_number:
        print("Oops Too low !!!")
    elif guess > secret_number:
        print("Ohh Too High !!!")
    else:
        print("Yup You Guessed It Right Congrats :).")
        print("You took " + str(tries) + " attemtps to guess the number.")

