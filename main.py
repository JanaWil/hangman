import data
import random

# create words to guess
words = ['FRIDGE', 'PYTHON', 'RIVER', 'FlOWER', 'NEIGHBOOR']
word = random.choice(words)

# document wrong guesses in a list
wrong_guesses = []

# display partial solution of the word
partial_solution = len(word) * "_"

# print gallow (from data.py) and partial solution
print(data.gallows[len(wrong_guesses)]) # gallow with the index of the number of wrong guesses
print(f"Your word: {partial_solution}")
