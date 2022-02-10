import random
check = True
win_count = 0 
# include a win count for some fun
wmsg = "Welcome to my rock paper scissors game!"
print(wmsg)
while check:
    selection = input("Please enter your selection:\n").upper()
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
    print(f"The computer throws {competition.lower().capitalize()}")
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
    play_again = input("Play again?(Y/N)\n").upper()
    print(play_again != "Y")
    # not equal to correct choice then loops through till proper choicen entered
    while play_again != "Y" or "N":
        play_again = input("Sorry, wrong selection entered. Please enter either a Y for yes, or N for no.\n").upper()
    if play_again == "Y":
        check = True
    elif play_again == "N":
        check = False
# print thank you message and win count
print(f"You won a total of {win_count} times!\n\
    Thank you for playing!")