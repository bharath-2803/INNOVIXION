import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 20. Try to guess it.")

    # Generate a random number between 1 and 20
    secret_number = random.randint(1, 20)

    # Set the maximum number of attempts
    max_attempts = 5

    for attempt in range(1, max_attempts + 1):
        # Get user input for the guess
        user_guess = int(input("Enter your guess: "))

        # Check if the guess is correct
        if user_guess == secret_number:
            print(f"Congratulations! You guessed the correct number in {attempt} attempts.")
            break
        elif user_guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

        # Check if the user has used all attempts
        if attempt == max_attempts:
            print(f"Sorry, you've run out of attempts. The correct number was {secret_number}. Better luck next time.")

# Run the game
number_guessing_game()


