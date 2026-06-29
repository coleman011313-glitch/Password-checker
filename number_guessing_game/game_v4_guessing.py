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


def play_game():
    max_number, attempts_left = choose_difficulty()
    secret_number = random.randint(1, max_number)

    score = 100

    print("\nI'm thinking of a number...")

    while attempts_left > 0:
        guess = int(input("Enter your guess: "))
        attempts_left -= 1

        if guess == secret_number:
            print("Correct! 🎉")
            print("Your score:", score)
            return
        elif guess > secret_number:
            print("Too high 📈")
        else:
            print("Too low 📉")

        score -= 10
        print("Attempts left:", attempts_left)

    print("Game over 😢 The number was", secret_number)


while True:
    play_game()

    again = input("\nPlay again? (y/n): ")
    if again.lower() != "y":
        break
