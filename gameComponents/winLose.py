from gameComponents import gameVars

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
		# reset the game and start over again
		gameVars.player_lives = 1
		gameVars.computer_lives = 1
		gameVars.player = False

	elif choice == "N" or choice == "n":
		# exit message and quit
		print("You chose to quit. Better luck next time!")
		exit()
	else:
		print("Make a valid choice - Y or N")
		# this is generating a bug -> need to fix this check
		choice = input("Y / N")