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

while len(wrong_guesses) < len(data.gallows) - 1:
    letter = input("Your guess: ").upper()
    if letter in word:
        pass #TODO: handle correctly guessed characters
    else:
        if letter not in wrong_guesses:
            wrong_guesses.append(letter)
    print(data.gallows[len(wrong_guesses)])
    print(f"Your word: {partial_solution}, Wrong guesses: {', '.join(wrong_guesses)}")
