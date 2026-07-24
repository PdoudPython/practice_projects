import random

def get_valid_guess():
    """Ask the user for a guess, keep asking until it's a valid integer."""
    while True:
        try:
            user_guess = int(input("What's your guess? "))
            return user_guess
        except ValueError:
            print("Please select a valid integer")

def play_round(lower, upper):
    """Play one round of the guessing game within a given range."""
    secret_number = random.randint(lower, upper)
    guesses = 0

    while True:
        guess = get_valid_guess()
        guesses += 1

        if guess > secret_number:
            print("Nope, too high!")
        elif guess < secret_number:
            print("Nope, too low!")
        else:
            print(f"Congratulations! You win! It took you {guesses} guesses!")
            break

def choose_difficulty():
    """Let the player pick a difficulty, which changes the number range."""
    difficulty_setting = 0
    while True:
        try:
            difficulty = int(input("What Difficulty would you like to try? 1. Easy (1-50)  2. Medium (1-100)  3. Hard (1-500) "))
            if difficulty == 1:
                difficulty_setting = (1, 50)
            elif difficulty == 2:
                difficulty_setting = (1, 100)
            elif difficulty == 3:
                difficulty_setting = (1, 500)
            else:
                raise ValueError("Please select a numebr 1 - 3. ")
            return difficulty_setting
        except ValueError:
            print("Please select a number 1 - 3. ")

            

def main():
    print("Welcome to the Guessing Game!")
    lower, upper = choose_difficulty()
    print(f"I'm thinking of a number between {lower} and {upper}...")

    play_round(lower, upper)

    while True:
        play_again = input("Would you like to play again? yes/no ").strip().lower()
        if play_again not in ['yes', 'no']:
            print("Invalid choice, please choose 'yes' or 'no': ")
        elif play_again == 'yes':
            lower, upper = choose_difficulty()
            print(f"I'm thinking of a number between {lower} and {upper}...")
            play_round(lower, upper)
        else:
            print("Thank you for playing! You may close the window")
            break
if __name__ == "__main__":
    main()