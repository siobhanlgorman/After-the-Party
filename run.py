import time

# gets user's name

print("Hello there!")
time.sleep(1)
player_name = input("What's your name?\n(Type your name)\n")
time.sleep(2)
print(f"Hi {player_name}!\n")
time.sleep(2)
print("OK, let's start the game.\n")

time.sleep(2)

friend_name = {}


# function to set scene and start game

def intro_bedroom():
    print("You wake up in an unfamiliar room as dawn is breaking.\n")
    time.sleep(2)
    print("Bit of a headache.\n")
    print("Whose house is this again?\n")
    time.sleep(2)
    print("Oh yes ... that new guy ... Jay, wasn't it?\n") 
    print("Great party last night though.\n")
    time.sleep(2)
    print("Hmmm..Shouldn't really have been partying what with that virus spreading and everything. \n")
    time.sleep(2)
    print("You realise the bed beside you is empty.\n")

    #user assigns global friend name
    global friend_name
    friend_name = input(f"{player_name}, who did you come to the party with?\n (Enter a name)\n")
    time.sleep(2)
    print(f"Where has {friend_name} got to??\n")
    time.sleep(2)
    print("Sleepwalking again probably.\n")
    time.sleep(2)
    print("You hear some groaning from outside.\n")
    time.sleep(2)
    print("You look out the window and see a couple of people from the party shuffling around the driveway near your car.\n")
    time.sleep(2)
    print("Must've had too much to drink.\n")
    time.sleep(2)
    print("They don't look at all well.\n")
    time.sleep(2)
    print("Very pale.\n")
    time.sleep(2)
    print("Better head off anyway.\n")
    time.sleep(2)
    print("(You pull on your clothes and look around the room\n")
    time.sleep(2)
    print("Which way out?\n")
    time.sleep(2)
    print("There are two doors in the bedroom. One is on the left and one on the right.\n")
    
    # user chooses left or right door
    door_choice = (input("Which do you choose? Left or Right\n").lower())
    if "l" in door_choice:
        print("You chose the door on the left")
        left_bathroom()
    elif "r" in door_choice:
        print("You chose the door on the right")
    else:
        print(input("Please enter left or right"))

def left_bathroom():
    print("You open the door. Just the bathroom. Before you go back out you notice a shape behind the shower curtain.\nWhat the ...??")
    choice = (input("Do you open the curtain? Yes or No\n").lower())
    if "y" in choice:
        you_die(f"Looks like you found {friend_name} … except it’s not {friend_name} any more....AGGGGHHHHHHH... Their skin is rotting and their eyes are white… they sink their teeth into your neck… YOU DIE")
    elif "n" in choice:
        print("You picked no. \n")
        time.sleep(2)
        print("You go back into the bedroom and open the other door")
        bedroom_1()
        time.sleep

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
        intro_bedroom()
    elif "n" in answer:
        print("No worries. Come back soon!")



#def bedroom_1():

#def camping_box():

#def upstairs():

#def downstairs():


#def run_game():
    #intro()
    #bedroom()

intro_bedroom()
