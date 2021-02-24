choices = { "R":,Rock "P": Paper, "S: Scissors" }

# Get the user's choice of the three
user_choice = input("\nType R, P, or S to play against the computer: ")

# Print what the user's choice, so she knows what she picked
print user_choice

# Make sure the user input is valid
if user_choice in choices:
   print "You chose %s." % user_choice
else:
   print "Your choice of %s is not a valid choice." % user_choice

