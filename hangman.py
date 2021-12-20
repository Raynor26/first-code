from random import choice 


# Words that can be selected as the primary word
possible_words = ['song', 'dangerous', 'justice']
# A list to hold wrong guesses
wrong_guesses = []
# A list to hold correct guesses
correct_guesses = []
# a list to hold how many guesses have been attempted
guess_counters = len(wrong_guesses)

# Boolean flag to activate/deactivate the game script
alive = True
# Flag to operate selected word function
wrong_input = True

def selected_word():
	"""A function to choose a random word from a set list"""
	word = choice(possible_words)
	return word

def user_guess():
	"""A function that prompts the user for a guess if they have enough guess tokens"""
	if guess_counters <= 8:
		wrong_input = True
		while wrong_input:
			letter = input("Please pick a letter: ").lower()
			if len(letter) != 1:
				print("\n\tPlease pick a single letter\n\n")
			elif letter in correct_guesses or letter in wrong_guesses:
				print("\n\tYou have already guessed that, please select again\n\n")
			elif not letter.isalpha():
				print("\n\tPlease select a letter\n\n") 
			else:
				wrong_input = False
	return letter

def check_guess(letter):
	"""Check to see if the letter is in the word"""
	print(letter)
	if letter in the_word:
		print(f"\n\tYes, {letter} is in the word!\n\n")
		correct_guesses.append(letter)
	else:
		print(f"\n\tSorry, {letter} is not in the word\n\n")
		wrong_guesses.append(letter)
		
def status_update():
	"""Lets the player know how many guesses they have left and what letters are correct and incorrect"""
	if _guesses_left() > 0:
		print(f"Guesses left: {_guesses_left()}")
		print(f"These letters are not in the word: {wrong_guesses} ")
		print(f"These letters are in the word: {correct_guesses} ")
	elif _guesses_left() <= 0:
		print("\tSorry, you've been hung!!!\n\n")
		print(f"The word was '{the_word.upper()}'. Better luck next time!")
		alive = False

def _guesses_left():
	"""A support function to calculate the number of guesses left"""
	lives = 8 - len(wrong_guesses)
	return lives

def _win_check():
	"""Check if the player has won the game"""
	if len(correct_guesses) == len(the_word):
		print(f"Well done, you have guessed all the letters!\n The word is {the_word.upper()}!")


the_word = selected_word()
print(the_word) # Used to test code, NEEDS REMOVING!!!!!!
while alive:
	_win_check()
	status_update()
	letter = user_guess()
	check_guess(letter)











