import time

# Empty list to hold weapons and tools selected by player
inventory = []
# Friend's name will be selected by player
friend_name = {}
# Party host name to be selected by player
host_name = {}

# welcome and get user's name

print("Hello there!")
time.sleep(1)
player_name = input("What's your name?\n>\n").capitalize()
time.sleep(2)
print(f"Hi {player_name}!\n")
time.sleep(2)
print("OK, let's start the game.\n")
time.sleep(1)


# function to set scene and start game

def intro():
    print("You wake up in an unfamiliar room as dawn is breaking.\n")
    time.sleep(2)
    print("Bit of a headache.\n")
    print("Whose house is this again?\n")
    time.sleep(0.5)
    global host_name
    host_name = (input(f"{player_name} who's party was it?\n").capitalize())
    print(f"Oh yes {host_name}'s party - they just moved here ...\n")
    print("Great party last night though.\n")
    time.sleep(2)
    print("Hmmm..Shouldn't really have been partying what with that virus spreading and everything. \n")
    time.sleep(2)
    print("You hear some groaning from outside.\n")
    time.sleep(2)
    print("You look out the window.\n")
    time.sleep(1)
    print("There's a couple of people from the party shuffling around the driveway near your car.\n")
    time.sleep(2)
    print("Must've had too much to drink.\n")
    time.sleep(2)
    print("They don't look at all well.\n")
    time.sleep(2)
    print("Very pale.\n")
    bedroom()

def bedroom():
    print("You notice the bed is empty.\n")

    # user assigns global friend name
    global friend_name
    friend_name = input(f"{player_name}, who did you come to the party with?\n").capitalize()
    time.sleep(2)
    print("That's funny...")
    time.sleep(1)
    print(f"Where has {friend_name} got to??\n")
    time.sleep(2)
    print("Sleepwalking again probably.\n")
    time.sleep(2)
    print("Better head off anyway.\n")
    time.sleep(1)
    print(f"{friend_name}'s probably downstairs\n")
    print("You pull on your clothes and look around the room\n")
    time.sleep(2)
    print("Which way out?\n")
    time.sleep(2)
    print("There are two doors in the bedroom. One is on the left and one on the right.\n")
    
    # user chooses left or right door
    door_choice = (input("Which do you choose? Left or Right\n").lower())
    if "l" in door_choice:
        print("You chose the door on the left\n")
        time.sleep(2)
        left_bathroom()
    elif "r" in door_choice:
        print("You chose the door on the right")
        landing()
    else:
        print(input("Please enter left or right"))

def left_bathroom():
    print("You open the door.\n")
    time.sleep(2)
    print("Just the bathroom.\n")
    time.sleep(2)
    print("Before you go back out you notice a shape behind the shower curtain.\n")
    time.sleep(1)
    print("What the ...??\n")
    choice = (input("Do you open the curtain? (Yes or No) \n"))
    if "y" in choice:
        print(f"Looks like you found {friend_name} …\n")
        time.sleep(2)
        print(f"except it’s not {friend_name} any more....\n")
        time.sleep(2)
        print("AGGGGGGGGHHHHHHHHHH...\n")
        time.sleep(1.5)
        print("Their skin is rotting and their eyes are white…\n")
        time.sleep(2)
        # attack or run choice?
        you_die(f"{friend_name} sinks their teeth into your neck… YOU DIE")
    elif "n" in choice:
        print("You picked no. \n")
        time.sleep(2)
        print("You go back into the bedroom and open the other door")
        bedroom_1()
        time.sleep
    else:
        print("Please choose yes or no")

def landing():
    print("You are now on the landing\n")
    camping_box = ["knife", "hammer", "tent peg", "rope", "frying pan", "nail scissors"]
    print("You come out of the bedroom onto the landing\n")
    print("There's a cardboard box marked 'camping equipment' just by the door.\n")
    answer = input("What do you do?\n")
    #if answer.lower() in ["box", "open", "look", "inside", "see"] :
        #print("you decided to open the box")
    #else:
        #input("I really think you should open the box")

def bedroom1():
    print("you are in bedroom1")
    
# function for when user dies and game ends
def you_die(reason):
    print(reason)
    time.sleep(2)
    play_again()

#function to ask user to play game again
def play_again():
    print("\nSorry you didn't make it home from the party.\n")
    time.sleep(2)
    answer = input("Do you want to try again? Yes or No\n")
    if "y" in answer:
        print("Good decision.\nYou can definitely make it out this time!\n")
        print("Good luck!\n")
        intro()
    elif "n" in answer:
        print("No worries. Come back soon!")




#def camping_box():

#def upstairs():
    # print("you are upstairs")

#def downstairs():
    # print("you are downstairs")


# function to start game
intro()
