import random

# List of words to choose from
words = ['python', 'hangman', 'programming', 'developer', 'computer', 'algorithm', 'function', 'variable']

def display_word(word, guessed_letters):
    """Display the word with underscores for unguessed letters."""
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    # Select a random word from the list
    word = random.choice(words)
    guessed_letters = []  # List to store guessed letters
    incorrect_guesses = 0  # Track the number of incorrect guesses
    max_incorrect_guesses = 6  # Set a limit for incorrect guesses

    print("Welcome to Hangman!")
    
    while incorrect_guesses < max_incorrect_guesses:
        print("\nWord to guess:", display_word(word, guessed_letters))
        print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")
        
        # Get the player's guess
        guess = input("Guess a letter: ").lower()
        
        # Check if the input is a valid single letter
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid letter.")
            continue
        
        # If the letter has already been guessed, inform the player
        if guess in guessed_letters:
            print(f"You've already guessed the letter '{guess}'. Try a different one.")
            continue
        
        guessed_letters.append(guess)

        # Check if the guess is correct
        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Oops! '{guess}' is not in the word.")
        
        # Check if the player has guessed the entire word
        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations! You've guessed the word: {word}")
            break
    
    # If the player runs out of incorrect guesses
    if incorrect_guesses == max_incorrect_guesses:
        print(f"\nYou've run out of guesses. The word was: {word}")
        print("Game Over!")

# Run the Hangman game
if _name_ == "_main_":
    hangman()
