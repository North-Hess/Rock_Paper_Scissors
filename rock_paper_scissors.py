import random
import time
check = True
win_count = 0
pause_value = 1
selection_list = ["ROCK", "PAPER", "SCISSORS"]
# include a win count for some fun
wmsg = "Welcome to my rock paper scissors game!"
print(wmsg)
time.sleep(pause_value)
while check:
    selection = input("Please enter your selection:\n").upper()
    selection_check = True
    if selection in selection_list:
        pass
    else:
    # not equal to correct choice then loops through till proper choicen entered
        selection_check = False 
        while selection_check == False:
            selection = input("Sorry, wrong selection entered. Please enter either rock, paper, or scissors (not case sensitive).\n").upper()
            if selection in selection_list:
                selection_check = True
    competition = random.randint(1,3)
    if competition == 1:
        competition = "ROCK"
    elif competition == 2:
        competition = "PAPER"
    elif competition == 3:
        competition = "SCISSORS"
    # 0 is a loss, 1 is a tie, 2 is a win 
    # assume loss and only check for changes to this
    result = 0
    if selection == "ROCK" and competition == "ROCK":
        result = 1
    elif selection == "ROCK" and competition == "SCISSORS":
        result = 2
    elif selection == "PAPER" and competition == "PAPER":
        result = 1
    elif selection == "PAPER" and competition == "ROCK":
        result = 2
    elif selection == "SCISSORS" and competition == "SCISSORS":
        result = 1
    elif selection == "SCISSORS" and competition == "PAPER":
        result = 2
    # display the choices of the computer and player
    print(f"You threw {selection.lower().capitalize()}")
    time.sleep(pause_value)
    print(f"The computer throws {competition.lower().capitalize()}")
    time.sleep(pause_value)
    # evaluate choices and print corresponding message
    if result == 0:
        print("The computer wins, so sorry for your loss")
    if result == 1:
        print("You both tied! Nobody wins today...")
    if result == 2:
        win_count += 1
        print("You won! Congratulations!")
    # check if the user wants to play again
    # using .upper so that the choice isn't case sensitive
    time.sleep(pause_value)
    play_again = input("Play again?(Y/N)\n").upper()
    continue_check = True
    if play_again == "Y" or play_again == "N":
        pass
    else:
    # not equal to correct choice then loops through till proper choicen entered
        continue_check = False 
        while continue_check == False:
            play_again = input("Sorry, wrong selection entered. Please enter either a Y for yes, or N for no.\n").upper()
            if play_again == "Y" or play_again == "N":
                continue_check = True
    if play_again == "Y":
        check = True
    elif play_again == "N":
        check = False
# print thank you message and win count
time.sleep(pause_value)
print(f"You won a total of {win_count} times!\n\
Thank you for playing!")