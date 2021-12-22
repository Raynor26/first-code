from random import choice 


# Words that can be selected as the primary word
possible_words = ['element', 'dangerous', 'justice', 'programmer', 'jolly', 'hello']
# A list to hold wrong guesses
wrong_guesses = []
# A list to hold correct guesses
correct_guesses = []

# Flag to run game script again or to quit game
play = True
# Boolean flag to activate/deactivate the main game script
alive = True
# Flag to operate selected word function
wrong_input = True

def selected_word():
	"""A function to choose a random word from a set list"""
	word = choice(possible_words)
	return word

def user_guess():
	"""A function that prompts the user for a guess if they have enough guess tokens"""
	while True:
		letter = input("\nPlease pick a letter: ").lower()
		if len(letter) != 1:
			print("\n\tPlease pick a single letter\n\n")
		elif letter in correct_guesses or letter in wrong_guesses:
			print("\n\tYou have already guessed that, please select again\n\n")
		elif not letter.isalpha():
			print("\n\tPlease select a letter\n\n") 
		else:
			break
	return letter

def check_guess(letter):
	"""Check to see if the letter is in the word"""
	if letter in the_word:
		print(f"\n\tYes, {letter} is in the word!\n\n")
		correct_guesses.append(letter)
	else:
		print(f"\n\tSorry, {letter} is not in the word\n\n")
		wrong_guesses.append(letter)
		
def status_update():
	"""Lets the player know how many guesses they have left and what letters are correct and incorrect"""
	print(f"\n\tGuesses left: {_guesses_left()}")
	print(f"\nThese letters are not in the word: {wrong_guesses} ")
	print(f"These letters are in the word: {correct_guesses}\n ")
	# Display the word as the player knows it so far
	_display_word()
	print(f"{status} {len(status)}")

def hung():
	"""If the player runs out of guesses this message gets shown"""
	print("\tSorry, you've been hung!!!\n\n")
	print(f"The word was '{the_word.upper()}'. Better luck next time!")
		
def _guesses_left():
	"""A support function to calculate the number of guesses left"""
	lives = 10
	lives -= len(wrong_guesses)
	return lives

def _win_check():
	"""Check if the player has won the game"""
	all_letters = True
	for l in the_word:
		if l not in correct_guesses:
			all_letters = False
			break
	if all_letters == False:
		return 'no'
	if all_letters == True:
		return 'yes'


def _display_word():
	"""Function to display the current state of the word"""
	for l in range(len(the_word)):
		if the_word[l] in correct_guesses:
			status[l] = the_word[l]

def attempt_guess():
	"""Allows the player a chance to guess the word at the cost of a life if its wrong"""
	answer = ("What is the word? ")
	if answer.lower() == the_word:
		print("YOU WIN!!!!!")
		return False
	else:
		lives -= 1

def win_script():
	"""Shows if the player has won"""
	print(f"Congratulations YOU WIN!!! The word was {the_word.upper()} \n\n")

def play_again():
	"""Asks the user if they would like to play again"""
	while True:
		replay = input("Would you like to play again? (y/n): ")
		if len(replay) != 1:
			print("\n\tPlease pick 'y' or 'n'\n")
		elif not replay.isalpha():
			print("\n\tPlease pick 'y' or 'n'\n")
		else:
			return replay
	if replay.lower() == 'y':
		return 'y'
	elif replay.lower() == 'n':
		return 'n'
def reset():
	"""Resets all the lists so the player has a fresh start"""
	wrong_guesses.clear()
	correct_guesses.clear()

def greeting():
	"""Greets the user when they open the app"""
	print("\n\n\n\t\t/// WELCOME TO HANGMAN ///\n\n")


# MAIN GAME LOOP
greeting()
while play:
	# Randomly selects a word for the list of options
	the_word = selected_word()
	# shows the current state of the word as the user knows it
	status = ["_"] * len(the_word)
	while alive:
		if _guesses_left() > 0:
			status_update()
		elif _guesses_left() <= 0:
			hung()
			break
		letter = user_guess()
		check_guess(letter)
		if _win_check() == 'yes':
			win_script()
			break
		else:
			continue
	
	if play_again() == 'y':
		reset()
		continue
	else:
		break
print("\nThank you for playing!\n")









