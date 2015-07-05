# "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import math
import simplegui
import random

secret_number = 0
number_guesses = 0
range_choice = 0


# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    global number_guesses
    global range_choice

    if range_choice == 0 or range_choice == 100:
        print "New Game. Range is from 0 to 100"
        number_guesses = 7
        secret_number = random.randrange(0,100)
    elif range_choice == 1000:
        number_guesses = 10
        print "New Game. Range is from 0 to 1000"
        secret_number = random.randrange(0,range_choice)

    frame.start()

# define event handlers for control panel
def range100():
    global range_choice
    range_choice = 100
    # button that changes the range to [0,100) and starts a new game
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game
    global range_choice
    range_choice = 1000
    new_game()


def input_guess(guess):
    # main game logic goes here
    global secret_number
    global number_guesses
    number_guessed = int(guess)
    print "Guess was ", number_guessed
    if number_guesses == 0:
        print "Number of remaining guesses", number_guesses
        print "You ran out of guesses. The number was ", secret_number
        new_game()
    else:
        if secret_number == number_guessed:
            print "Correct!"
            new_game()
        elif secret_number > number_guessed:
            number_guesses -= 1
            print "Number of remaining guesses", number_guesses
            print "Higuer"
        else:
            number_guesses -= 1
            print "Number of remaining guesses", number_guesses
            print "Lower"


# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame
frame.add_button("Range [0,100)", range100, 200)
frame.add_button("Range [0,1000)", range1000, 200)
frame.add_input("Guess the number!",input_guess, 100)


# call new_game
new_game()
