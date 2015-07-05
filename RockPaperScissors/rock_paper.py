# Rock-paper-scissors-lizard-Spock


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

import random

def name_to_number(name):
    # delete the following pass statement and fill in your code below
    # convert name to number using if/elif/else
    # don't forget to return the result!

    # Lower of name in order to validate cases like RoCk
    if name.lower() == 'rock':
        my_number = 0
    elif name.lower() == 'spock':
        my_number = 1
    elif name.lower() == 'paper':
        my_number = 2
    elif name.lower() == 'lizard':
        my_number = 3
    elif name.lower() == 'scissors':
        my_number = 4
    else:
        my_number = None
    return my_number


def number_to_name(number):
    # delete the following pass statement and fill in your code below
    #pass
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    if number == 0:
        my_name = 'rock'
    elif number == 1:
        my_name = 'Spock'
    elif number == 2:
        my_name = 'paper'
    elif number == 3:
        my_name = 'lizard'
    elif number == 4:
        my_name = 'scissors'
    else:
        my_name = None
    return my_name

def rpsls(player_choice):
    # delete the following pass statement and fill in your code below
    #pass

    # print a blank line to separate consecutive games
    print

    # print out the message for the player's choice
    print "Player chooses " + player_choice

    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)

    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,4)
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    # print out the message for computer's choice
    print 'Computer chooses ' + comp_choice
    # compute difference of comp_number and player_number modulo five
    difference = (comp_number - player_number) % 5
    # use if/elif/else to determine winner, print winner message
    if (difference == 1 or difference == 2):
        print "Computer Wins!"
    elif (difference == 3 or difference == 4):
        print "Player Wins!"
    else:
        print "Player and computer tie!"

# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric
