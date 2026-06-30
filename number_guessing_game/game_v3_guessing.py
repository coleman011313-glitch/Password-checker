import random

play_again = "y"

while play_again == "y":

    number = random.randint(1, 10)
    guess = None
    attempts = 0
    max_attempts = 5

    print("Welcome to the Guessing Game!")

    while guess != number and attempts < max_attempts:
        guess = int(input("Guess a number between 1 and 10: "))
        attempts += 1

        if guess == number:
            print("Correct!")
        elif guess > number:
            print("Too high")
        else:
            print("Too low")

        print("Attempts left:", max_attempts - attempts)

    if guess != number:
        print("Game over! The number was", number)

    play_again = input("Do you want to play again? (y/n): ")
