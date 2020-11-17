# import packages to extend python (just like we extend sublime, or Atom, or VSCode)
from random import randint


# create a variable stack - bits of data that can (and will) change

# [] => this is an array. an array is a special type of container that can hold multipe items
# arrays are indexed (their contents get assigned a number)
# the index always starts at 0
choices = ["rock", "paper", "scissors"]

player_lives = 5
computer_lives = 5

total_lives = 5

player = False; # True and False are Booleans - data types that can be truthy or falsy

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
		print("You lost! Loser. Would you like to play again?")
		choice = input("Y / N? ")

		if choice == "Y" or choice == "y":
			# reset the game and start over again
			player_lives = 2
			computer_lives = 2
			player = False

		elif choice == "N" or choice == "n":
			# exit message and quit
			print("You chose to quit. Better luck next time!")
			exit()
		else:
			print("Make a valid choice - Y or N")
			# this is generating a bug -> need to fix this check
			choice = input("Y / N")

	elif computer_lives is 0:
		print("You won! Winner. Would you like to play again?")
		choice = input("Y / N? ")

		if choice == "Y" or choice == "y":
			# reset the game and start over again
			player_lives = 2
			computer_lives = 2
			player = False

		elif choice == "N" or choice == "n":
			# exit message and quit
			print("You chose to quit. Better luck next time!")
			exit()
		else:
			# this is generating a bug -> need to fix this check
			print("Make a valid choice - Y or N")
			choice = input("Y / N")

	else:
		player = False
		# computer = choices[randint(0,2)]
