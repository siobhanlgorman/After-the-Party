import time

# introduces game and gets user's name

print("Hello there!")
time.sleep(1)
player_name = input("What's your name?\n")
time.sleep(1)
print(f"Hi {player_name}!\n")
time.sleep(1)


# set scene and start game

def intro_bedroom():
    print("You wake up in an unfamiliar room as dawn is breaking.\n Bit of a headache.\n Whose house is this again? \n Great party last night though.\n")
    print("You stretch.\n Probably shouldn't have gone to the party what with that virus spreading and everything. \n Sure it'll never reach us here ")
    print("Where the hell is Jay anyway? They crashed here too, didn't they\n")
    print("You hear some groaning from outside. You look out the window and see a couple of people from the party shuffling around the driveway near your car.\n Must've had too much to drink.\n")
    print("Better head off anyway.\n You pull on your clothes\n")
    print("There are two doors in the bedroom. One is on the left and one on the right.\n")
    
    door_choice = (input("Which do you choose? Left or Right\n").lower())
    if door_choice == "left":
        print("You chose the door on the left")
        left_bathroom()
    elif door_choice == "right":
        print("You chose the door on the right")
    else:
        print(input("Please enter left or right"))

def left_bathroom():
    print("You open the door. Just the bathroom. Before you go back out you notice a shape behind the shower curtain.\n")
    choice = (input("Do you open the curtain? Yes or No\n").lower())
    if choice == "yes":
        you_die("Looks like you found Jay … except it’s not Jay any more....AGGGGHHHHHHH... Their skin is rotting and their eyes are white… they sink their teeth into your neck… YOU DIE")
    elif choice == "no":
        print("You picked no")
    else:
        print("Please choose yes or no")
    
# function for when user dies and game ends
def you_die(reason):
    print(reason)
    play_again()

#function to ask user to play game again
def play_again():
    answer = input("Sorry you didn't make it out. Do you want to try again? Yes or No").lower()
    if "y" in answer:
        print("Good decision.\n You can definitely make it out! Good luck!\n")
        intro()


#def bathroom():

#def bedroom_1():

#def camping_box():

#def upstairs():

#def downstairs():


#def run_game():
    #intro()
    #bedroom()

intro_bedroom()
