
import random
from replit import clear
word_list = ["aardvark", "baboon", "camel"]
stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /    |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''']
fails = 0

chosen_word = word_list[random.randint(0, len(word_list) - 1)]
masked_word = []
for i in range(0, len(chosen_word)):
    masked_word += "_"

print(f"Welcome to the game of Hangman! The word is:\n{masked_word}\n")

while "_" in masked_word and not fails >= 6:
    guess = input("Guess a letter:\n").lower()
    clear()
    if guess in chosen_word:
        for position in range(len(chosen_word)):
            current_letter = chosen_word[position]
            if current_letter == guess:
                masked_word[position] = current_letter
    else:
        fails += 1
    print(stages[fails])
    print(f"{masked_word}\n")

if fails >= 6:
    print(f"Game over! No lives left. the word was {chosen_word}")
elif "_" not in masked_word:
    print("Game over! YOU WON!")