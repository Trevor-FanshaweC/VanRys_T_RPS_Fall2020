# import packages to extend python (just like we extend sublime, or Atom, or VSCode)
from random import randint


# create a variable stack - bits of data that can (and will) change

# [] => this is an array. an array is a special type of container that can hold multipe items
# arrays are indexed (their contents get assigned a number)
# the index always starts at 0
choices = ["rock", "paper", "scissors"]

player_lives = 1
computer_lives = 1

total_lives = 1

player = False; # True and False are Booleans - data types that can be truthy or falsy

# define a win / lose function and refer to it (invoke it) in our game loop
def winorlose(status):
	#print("called winorlose", status)

	if status == "won":
		pre_message = "You are the yuuuuuuugest winner ever! "
	else:
		pre_message = "You done trumped it, loser! "

	print(pre_message + "Would you like to play again?")
	
	choice = input("Y / N? ")

	if choice == "Y" or choice == "y":

		global player_lives
		global computer_lives
		global player
		# reset the game and start over again
		player_lives = 1
		computer_lives = 1
		player = False

	elif choice == "N" or choice == "n":
		# exit message and quit
		print("You chose to quit. Better luck next time!")
		exit()
	else:
		print("Make a valid choice - Y or N")
		# this is generating a bug -> need to fix this check
		choice = input("Y / N")

# set up our game loop
while player is False:
	# this is the player choice
	print("===============*/ RPS /*====================")
	print("Computer Lives:", computer_lives, "/", total_lives)
	print("Player Lives:", player_lives, "/", total_lives)
	print("===================================")
	print("Choose your weapon! or type quit to exit\n")
	player = input("Choose rock, paper or scissors: \n")

	# if the player chooses to quit, then don't do anything else
	# just exit the process (kill Python) and quit the game
	if player == "quit":
		print("You chose to quit, quitter!")
		exit()

	# this will be the AI choice -> a random pick from the choices array
	computer = choices[randint(0, 2)]

	# check to see what the user input

	# print outputs whatever is in the round brackets -> in this case it outputs player to the command prompt window
	print("user chose: " + player)

	# validate that the random choice worked for the AI
	print("AI chose: " + computer)

	if (computer == player):
		print("tie")

	# always check for negative conditions first (the losing case)
	elif (computer == "rock"):
		if (player == "scissors"):
			player_lives = player_lives - 1
			print("you lose! player lives: ", player_lives)
		else:
			print("you win!")
			computer_lives = computer_lives - 1

	elif (computer == "paper"):
		if (player == "scissors"):
			player_lives = player_lives - 1
			print("you lose! player lives: ", player_lives)
		else:
			print("you win!")
			computer_lives = computer_lives - 1


	elif (computer == "scissors"):
		if (player == "rock"):
			player_lives = player_lives - 1
			print("you lose! player lives: ", player_lives)
		else:
			print("you win!")
			computer_lives = computer_lives - 1

	# check player lives and AI lives
	if player_lives is 0:
		winorlose("lost")

	elif computer_lives is 0:
		winorlose("won")

	else:
		player = False
