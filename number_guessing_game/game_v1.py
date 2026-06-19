import random

number = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: 7  "))

if guess == number:
    print("Correct!")
elif guess > number:
    print("Too high")
else:
    Print("Too low")
