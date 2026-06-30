import random


def choose_difficulty():
    print("Choose difficulty:")
    print("1. Easy (1-10, 7 tries)")
    print("2. Medium (1-50, 10 tries)")
    print("3. Hard (1-100, 7 tries)")

    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        return 10, 7
    elif choice == "2":
        return 50, 10
    else:
        return 100, 7


def get_valid_guess(max_number):
    """
    Keeps asking the user until they enter a valid number
    within the correct range.
    """

    while True:
        try:
            guess = int(input(f"Enter your guess (1-{max_number}): "))

            if guess < 1 or guess > max_number:
                print("Out of range! Try again.")
                continue

            return guess

        except ValueError:
            print("Please enter a whole number.")


def play_game():
    max_number, attempts_left = choose_difficulty()
    secret_number = random.randint(1, max_number)

    score = 100

    print("\nI'm thinking of a number...")

    while attempts_left > 0:

        guess = get_valid_guess(max_number)

        attempts_left -= 1
        score -= 10

        if guess == secret_number:
            print("Correct! 🎉")
            print("Your score:", score)
            return

        elif guess > secret_number:
            print("Too high 📈")

        else:
            print("Too low 📉")

        print("Attempts left:", attempts_left)

    print("Game over 😢 The number was", secret_number)


while True:
    play_game()

    again = input("\nPlay again? (y/n): ")
    if again.lower() != "y":
        break
