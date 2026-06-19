import random

number = random.randint(1, 10)
guess = 0
attempts = 0

while guess != number and attempts < 5:
    guess = int(input("Guess a number between 1 and 10: "))
    attempts = attempts + 1

    if guess == number:
        print("Correct!")
    elif guess > number:
        print("Too high")
    else:
        print("Too low")

if guess != number:
    print("Game over! The number was", number)
