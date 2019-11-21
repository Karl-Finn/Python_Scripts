"""
Author: Karl Finnerty
Date: 20 November 2019
e-mail: karlfinnerty@protonmail.ch

Note: the word list used in this program was obtained from http://wordlist.sourceforge.net/ with credit to
      its creator/s
"""

import random

rope_dict = {6: """
    _______________
    |              |
    |
    |
    |
    |
    |
    |
-----------------------------
""",

             5: """
    _______________
    |              |
    |              O
    |
    |
    |
    |
    |
-----------------------------
""",

             4: """
    _______________
    |              |
    |              O
    |              |
    |              |
    |             
    |
    |
-----------------------------
""",
             3: """
    _______________
    |              |
    |              O
    |             \|
    |              |
    |             
    |
    |
-----------------------------
""",

             2: """
    _______________
    |              |
    |              O
    |             \|/
    |              |
    |
    |
    |
-----------------------------
""",

             1: """
    _______________
    |              |
    |              O
    |             \|/
    |              |
    |             / 
    |
    |
-----------------------------
""",

             0: """
    _______________
    |              |
    |              O
    |             \|/
    |              |
    |             / \\
    |
    |
-----------------------------
"""
             }

# Create a list of the words that are in words.txt
words_list = []
with open('hard_words.txt', 'r') as txt:
    for w in txt:
        words_list.append(w.strip())

# Strip any "'s" from these words and create a numbered dictionary of them
words_dict = {}
num = 1
for word in words_list:
    if "'s" in word:
        words_dict[num] = word.strip("'s")
        num += 1
    else:
        words_dict[num] = word
        num += 1

# Initialize Variables needed for the game logic
hangman_word = words_dict[random.randint(1, len(words_list))]

guessed_word_str = "*" * len(hangman_word)

guessed_word_list = [i for i in guessed_word_str]

num_guesses = 6

wrong_letters = ''
print(hangman_word)


# Game Logic
while guessed_word_str != hangman_word:
    if num_guesses > 0:
        print(f"Guesses remaining: {num_guesses}")
        print(rope_dict[num_guesses])
        print(f"Word: {guessed_word_str}")
        print(f"Wrong letters guessed: {wrong_letters}")

        guessed_letter = input("Guess a letter: ")
        guessed_letter = guessed_letter.lower()
        print("\n")

        # Check if the guess was an alphabetic character
        if not guessed_letter.isalpha():
            print(f"You guessed: {guessed_letter}\nPlease enter only letters.")

        # if the guessed letter is in the hangman word
        elif guessed_letter in hangman_word:
            for index, letter in enumerate(hangman_word):
                if letter == guessed_letter:
                    guessed_word_list[index] = guessed_letter
                    guessed_word_str = ''
                    for e in guessed_word_list:
                        guessed_word_str += e
        # if the guessed letter is not in the hangman word but has already been guessed previously
        elif guessed_letter in wrong_letters:
            print(f"You guessed '{guessed_letter}' already.")
            continue
        # if the guessed letter is not in the hangman word and has not been guessed previously
        else:
            wrong_letters += f"{guessed_letter},"
            num_guesses -= 1
    else:  # Runs if there are no guesses left for the player
        print("GAME OVER!")
        print(rope_dict[num_guesses])
        print(f"The word was: {hangman_word}")
        break
else:  # runs if and when the 'while' is False
    print("YOU WIN!")
