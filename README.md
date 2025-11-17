# ba-cs-hangman
Bridge Academy Computer Science Hangman Activity

A word will be chosen randomly from a list of words that are stored in the program
Each player will get 8 incorrect guesses to guess the word
At the beginning of the game, you will display a welcome message and the initial info: 
Welcome – Let’s Play Hangman!
Take your first turn:

Before each guess, display the characters that have been guessed already, a display of the word showing letters guessed and unknown letters, and the number of incorrect guesses remaining. At each turn, the user will select a letter.
Example: 
You have 6 incorrect guesses remaining
C H _ _ S _ _ _ S
	Incorrect letters guessed: Z Q
Guess a Letter:

When the player guesses a letter, make sure it has not already been guessed. If it has already been guessed, ask for another letter. 
If the letter is found, respond with how many instances of this letter is in the word, and go to the next turn. 
Guess a Letter: o
1 O in the word!

_ O _ 
Incorrect letters guessed: 
Guess a Letter:

If the letter is not found, inform player, decrement the number of guesses, and go to the next turn. 
Sorry Z is not in the word. Try again. 

You have 7 incorrect guesses remaining
_ O _ 
Incorrect letters guessed: Z 
Guess a Letter:

If the player selects all of the letters, inform them that they won, tell how many remaining incorrect guesses they had, and end the game. 
That’s Correct – You WIN! 
You had 3 guesses remaining

If the player does not select all the letters in the word before running out of guesses, inform the player and end the game.
Sorry, you lose. The word was DOG. Please play again! 

