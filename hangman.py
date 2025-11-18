# hangman.py
# This is our main program file for the Hangman activity

from hang_words import wordList

#initial setup
num_guesses = 8
word = " "
incorrect = []
correct = []

# choose our word

wordSet = set(wordList)
word = wordSet.pop()

print(word)