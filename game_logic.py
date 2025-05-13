import random
from ascii_art import STAGES

WORDS = ["python", "git", "github", "snowman", "meltdown"]
MAX_MISTAKES = len(STAGES) - 1

def get_random_word():
    """Selects a random word from the list."""
    return random.choice(WORDS)

def display_game_state(mistakes, secret_word, guessed_letters):
    """
    displays the game state including changes in case of correctly guessed letters.
    """
    print(STAGES[mistakes])
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word:", display_word.strip())
    print("Guessed Letters:", " ".join(sorted(guessed_letters)))
    print("\n")

def play_game():
    """
    game loops as long as MAX_MISTAKES has not been reached.
    """
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")

    while mistakes < MAX_MISTAKES:
        display_game_state(mistakes, secret_word, guessed_letters)
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single valid letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            print(f"Oops! '{guess}' is not in the word.")
            mistakes += 1
        else:
            print(f"Good job! '{guess}' is in the word.")

        if all(letter in guessed_letters for letter in secret_word):
            display_game_state(mistakes, secret_word, guessed_letters)
            print("You saved the snowman! You win!")
            break
    else:
        display_game_state(mistakes, secret_word, guessed_letters)
        print(f"The snowman melted... The word was '{secret_word}'. Better luck next time!")


if __name__ == "__main__":
    play_game()