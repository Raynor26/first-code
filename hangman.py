from random import choice 

# Alphabet for giving letters
alphabet = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
# Words that can be selected as the primary word
possible_words = ['element', 'dangerous', 'justice', 'programmer', 'jolly', 'hello', 'panther', 'mercury', 'random',
'fluffy', 'generate', 'enforcer', 'tackle', 'blurry']
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
	possible_words.remove(word)
	return word

def user_guess():
	"""A function that prompts the user for a guess if they have enough guess tokens"""
	while True:
		letter = input("\nPlease pick a letter: ").lower()
		if letter == 'answer':
			break
		elif len(letter) != 1:
			print("\n\tPlease pick a single letter\n\n")
		elif letter in correct_guesses or letter in wrong_guesses:
			print("\n\tYou have already guessed that, please select again\n\n")
		elif not letter.isalpha():
			print("\n\tPlease select a letter\n\n") 
		else:
			break
	return letter

def attempt_answer():
	"""Allows the player the opportunity to take a guess at the answer but loses a guess if its wrong"""
	attempt = input("\nWhat do you think the word is? ")
	if attempt.lower() == the_word:
		return 'win'
	else: 
		return 'lose'

def check_guess(letter, token):
	"""Check to see if the letter is in the word"""
	if letter in the_word:
		print(f"\n\tYes, {letter} is in the word!\n")
		correct_guesses.append(letter)
		token = 0
		return token
	else:
		print(f"\n\tSorry, {letter} is not in the word\n")
		wrong_guesses.append(letter)
		token += 1
		return token
		
def status_update():
	"""Lets the player know how many guesses they have left and what letters are correct and incorrect"""
	print(f"\tGuesses left: {_guesses_left(lives)}")
	print(f"\nThese letters are not in the word: {wrong_guesses} ")
	print(f"These letters are in the word: {correct_guesses}\n ")
	# Display the word as the player knows it so far
	_display_word()
	print(f"{status}  {len(status)} letter word")

def hung():
	"""If the player runs out of guesses this message gets shown"""
	print("\tSorry, you've been hung!!!\n\n")
	print(f"The word was '{the_word.upper()}'. Better luck next time!")
		
def _guesses_left(guesses):
	"""A support function to calculate the number of guesses left"""
	lives = guesses 
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

def win_script():
	"""Shows if the player has won"""
	print(f"\nCongratulations YOU WIN!!! The word was {the_word.upper()} \n")

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
	print("\n\n\n\t\t\t/// WELCOME TO HANGMAN ///\n")
	print("\tYou can type 'answer' at any time to attempt to guess the word!\n\tBe careful though, you will lose a life if you get it wrong.\n\n")

def hint(token):
	working_alphabet = []
	if token >= 3:
		print("Here is a helping hand, 1 free letter")
		for l in the_word:
			if l in alphabet:
				working_alphabet.append(l)
		for l in working_alphabet:
			if l in correct_guesses:
				working_alphabet.remove(l)
		working_alphabet = list(set(working_alphabet))
		new_letter = choice(working_alphabet)
		correct_guesses.append(new_letter)
		return False

# MAIN GAME LOOP
greeting()
while play:
	# Sets values for initial lives and hint tokens
	token = 0
	lives = 10
	# Randomly selects a word for the list of options
	the_word = selected_word()
	# shows the current state of the word as the user knows it
	status = ["_"] * len(the_word)
	
	while alive:
		if _guesses_left(lives) > 0:
			status_update()
		elif _guesses_left(lives) <= 0:
			hung()
			break
		letter = user_guess()
		if letter == 'answer':
			result = attempt_answer()
			if result == 'win':
				win_script()
				break
			elif result == 'lose':
				lives -= 1
				continue
		token = check_guess(letter, token)
		if hint(token) == False:
			token = 0
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









