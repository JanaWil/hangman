import data
import random

"""
create words to guess
"""
words = ['FRIDGE', 'PYTHON', 'RIVER', 'FLOWER', 'NEIGHBOOR']
word = random.choice(words)

"""
create list to document wrong guesses in a list
"""
wrong_guesses = []

"""
create display of partial solution of the word
"""
partial_solution = len(word) * "_"

"""
print gallow (from data.py) and partial solution
"""
print(data.gallows[len(wrong_guesses)]) # gallow with the index of the number of wrong guesses
print(f"🎯 Your word: {partial_solution}")

"""
while guesses left & word not fully guessed yet, ask for input and give feedback
"""
while len(wrong_guesses) < len(data.gallows) - 1 and partial_solution != word:
    letter = input("Your guess: ").upper() # get letter as an input
    if letter in word:
        for i, x in enumerate(word):
            if x == letter:
                partial_solution = partial_solution[:i] + letter + partial_solution[i+1:]
    else:
        if letter not in wrong_guesses: # check whether wrong letter was guessed before and add to wrong guesses list
            wrong_guesses.append(letter)
    print(data.gallows[len(wrong_guesses)])
    print(f"🎯 Your word: {partial_solution}")
    print(f"❌ Wrong guesses: {', '.join(wrong_guesses)}")
    print(f"✅ Number of guesses still left: {len(data.gallows) - len(wrong_guesses) - 1}\n")

"""
give feedback whether the game was won or lost
"""
if word == partial_solution:
    print("Congrats, you have won!\n")
else:
    print(f"Oh no, you have lost! The word was: {word}\n")
