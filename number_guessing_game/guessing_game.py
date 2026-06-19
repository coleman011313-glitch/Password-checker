import random

number = random.randint(1, 10)
guess = 0
attempts = 0

def check_guess(guess, number):
    if guess == number:
        print("Correct!")
    elif guess > number:
        print("Too high")
    else:
        print("Too low")

number = random.randint(1, 10)
guess = None
attempts = 0 
max_attempts = 5

print("Welcome to the Guessing game!")

while guess !=number and attempts < max_attempts:
    guess = int(input("Guess a number between 1 and 10: "))
    attempts += 1

    check_guess(guess, number )
    print("Attempts left:", max_attempts - attempts)

if guess != number:
    print("Game over! The number was", number)
