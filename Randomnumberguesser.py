import random
print("----------------------")
print("Welcome to the number guessing game!")
print("Here you will enter a number from 1 to 50, and with hints, you need to guess the random number that the pc decided")
print("----------------------")
pcnumber = random.randint(1, 50)
guesses = 0

t = True
while t:
    numberguess = int(input("Guess a number (1 - 50): "))
    if numberguess == pcnumber:
        print("----------------------")
        print("You won, the number was", pcnumber)
        print("You guessed", guesses, "times!")
        print("----------------------")
        t = False
    elif pcnumber <= numberguess:
        print("Lower!")
    elif pcnumber >= numberguess:
        print("Higher!")
    guesses = guesses + 1