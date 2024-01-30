# import random

# def hangman():
#     words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']
#     word = random.choice(words)
#     guessed_letters = []
#     turns = 10

#     while turns > 0:
#         guessed_word = ''
#         for letter in word:
#             if letter in guessed_letters:
#                 guessed_word += letter
#             else:
#                 guessed_word += '-'

#         print(f"Word: {guessed_word}")
#         print(f"Turns left: {turns}")

#         if guessed_word == word:
#             print("Congratulations! You guessed the word.")
#             return

#         guess = input("Enter a letter: ").lower()

#         if guess in guessed_letters:
#             print("You already guessed that letter. Try again.")
#         elif guess in word:
#             print("Correct guess!")
#             guessed_letters.append(guess)
#         else:
#             print("Wrong guess!")
#             turns -= 1
#             guessed_letters.append(guess)

#     print("Game over! You ran out of turns.")
#     print(f"The word was: {word}")

# hangman()

import random

def choose_word(word_list):
    """Randomly choose a word from the list."""
    return random.choice(word_list)

def display_current_progress(word, guessed_letters):
    """Display the current progress of the word based on guessed letters."""
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman_game(word_list):
    # Choose a random word
    word = choose_word(word_list).upper()
    guessed_letters = set()
    attempts = 10

    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")
    print(display_current_progress(word, guessed_letters))

    while attempts > 0:
        guess = input("Guess a letter: ").upper()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.add(guess)
            print("Good guess!")
        else:
            guessed_letters.add(guess)
            attempts -= 1
            print(f"Oops! That letter is not in the word. You have {attempts} attempts left.")

        current_progress = display_current_progress(word, guessed_letters)
        print(current_progress)

        if '_' not in current_progress:
            print("Congratulations! You've won!")
            return

    print(f"Game over! The word was {word}.")

# Example word list
words = ["python", "hangman", "computer", "programming", "developer"]

# Running the game
hangman_game(words)


