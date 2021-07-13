import time

# gets user's name

print("Hello there!")
time.sleep(1)
player_name = input("What's your name?\n")
time.sleep(1)
print(f"Hi {player_name}!\n")
time.sleep(1)

friend_name = {}
host_name = {}

# set scene and start game

def intro_bedroom():
    print("You wake up in an unfamiliar room as dawn is breaking.\nBit of a headache.\nWhose house is this again? \nGreat party last night though.\n")
    time.sleep(1)
    print("You stretch.\n Probably shouldn't have gone to the party what with that virus spreading and everything. \n Sure it'll never reach us here ")
    time.sleep(1)
    global friend_name
    friend_name = input(f"{player_name}, who did you come to the party with?")
    print(f"Where the hell is {friend_name} anyway?\n")
    time.sleep(1)
    print("You hear some groaning from outside. You look out the window and see a couple of people from the party shuffling around the driveway near your car.\n Must've had too much to drink.\n")
    time.sleep(1)
    print("Better head off anyway.\n You pull on your clothes and look around the room\n")
    time.sleep(1)
    print("There are two doors in the bedroom. One is on the left and one on the right.\n")
    print(player_name)
    
    door_choice = (input("Which do you choose? Left or Right\n").lower())
    if "l" in door_choice:
        print("You chose the door on the left")
        left_bathroom()
    elif "r" in door_choice:
        print("You chose the door on the right")
    else:
        print(input("Please enter left or right"))

def left_bathroom():
    print("You open the door. Just the bathroom. Before you go back out you notice a shape behind the shower curtain.\n")
    choice = (input("Do you open the curtain? Yes or No\n").lower())
    if "y" in choice:
        you_die(f"Looks like you found {friend_name} … except it’s not {friend_name} any more....AGGGGHHHHHHH... Their skin is rotting and their eyes are white… they sink their teeth into your neck… YOU DIE")
    elif "n" in choice:
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
    elif "n" in answer:
        print("No worries. Come back soon!")


#def bathroom():

#def bedroom_1():

#def camping_box():

#def upstairs():

#def downstairs():


#def run_game():
    #intro()
    #bedroom()

intro_bedroom()
