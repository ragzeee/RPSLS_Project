# Rock Paper Scissors Lizard Spock

print("""The Rules of the Game are:

    Scissors cuts Paper
    Paper covers Rock
    Rock crushes Lizard
    Lizard poisons Spock
    Spock smashes Scissors
    Scissors decapitates Lizard
    Lizard eats Paper
    Paper disproves Spock
    Spock vaporizes Rock
    Rock crushes Scissors""")

import time
    #importing the time module

time.sleep(5.00)
    #wait for 5 seconds    

print()

name = input("What is your name? ")
    #welcoming the user

print ("Hello " + name+ ", time to play Rock Paper Scissors Lizard Spock!")
    #greeting

print (" ")

time.sleep(1.00)
    #wait for 1 second    

    # to import random function for using random.randrange
import random

    # function to convert number to name
def number_to_name(number):
    if number == 0:
        return "rock"

    elif number == 1:
        return "spock"

    elif number == 2:
        return "paper"

    elif number == 3:
        return "lizard"

    elif number == 4:
        return "scissors"

    else:
        return "Error"

    # function to convert name to number
def name_to_number(name):
    if name == "rock":
        return 0

    elif name == "spock":
        return 1

    elif name == "paper":
        return 2

    elif name == "lizard":
        return 3

    elif name == "scissors":
        return 4

    else:
        print (name + " is not a character in RPSLS")

    # function which selects the winner
def rpsls(guess): 
        
        # convert name to player_number using name_to_number
    player_number = name_to_number(guess)
        
        # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)

        # compute difference of player_number and comp_number modulo five
    winner = (comp_number - player_number) % 5

        # use if/elif/else to determine winner
    if winner < 3:
        player_win = False
    else:
        player_win = True
        
        # convert comp_number to name using number_to_name
    comp_name = number_to_name(comp_number)
        
        # print results
    print ("Player chooses " + guess)
    print ("Computer chooses " + comp_name)
    if player_win:
        print ("Player wins!\n")
    elif comp_number == player_number:
        print ("Player and computer tie!\n")
    else:
        print ("Computer wins!\n")
        
player_guess = input('Enter your choice... Options: rock, paper, scissors, lizard, spock: ')

rpsls(str(player_guess))

print('Thank you for playing!!')