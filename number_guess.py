import random

def get_valid_guess():
    """Ask the user for a guess, keep asking until it's a valid integer."""
    while True:
        # TODO: try to convert input() to an int
        # TODO: if it fails, print an error and loop again
        # TODO: if it works, return the int
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

        # TODO: compare guess to secret_number
        # TODO: if too low, print "Too low!"
        # TODO: if too high, print "Too high!"
        # TODO: if correct, print how many guesses it took, then return/break

        if guess > secret_number:
            print("Nope, too high!")
        elif guess < secret_number:
            print("Nope, too low!")
        else:
            print(f"Congratulations! You win! It took you {guesses} guesses!")
            break

def choose_difficulty():
    """Let the player pick a difficulty, which changes the number range."""
    # TODO: print options like "1. Easy (1-50)  2. Medium (1-100)  3. Hard (1-500)"
    # TODO: return a (lower, upper) tuple based on their choice
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

    # TODO: ask if they want to play again, loop if yes
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