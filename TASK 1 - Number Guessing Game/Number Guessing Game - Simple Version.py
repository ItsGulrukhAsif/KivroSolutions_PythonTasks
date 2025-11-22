import random

def number_guessing_game():
    print("🎯 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 10...")

    # Generate a random number between 1 and 10
    secret_number = random.randint(1, 10)

    while True:
        try:
            guess = int(input("Enter your guess (1–10): "))
        except ValueError:
            print("⚠️ Please enter a valid number.")
            continue

        # Check if guess is within range
        if guess < 1 or guess > 10:
            print("❌ Out of range! Please guess between 1 and 10.")
            continue

        # Compare guess to the secret number
        if guess < secret_number:
            print("🔻 Too low! Try again.")
        elif guess > secret_number:
            print("🔺 Too high! Try again.")
        else:
            print("✅ Correct! You guessed the number!")
            break

    print("🎉 Thanks for playing! Goodbye!")

# Run the game
if __name__ == "__main__":
    number_guessing_game()




