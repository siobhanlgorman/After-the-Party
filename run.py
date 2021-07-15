import time

# Empty list to hold weapons and tools selected by player
inventory = []


def welcome():
    """
    welcome and get user's name
    """
    print("Hello there!")
    time.sleep(1)
    player_name = input("What's your name?:\n").capitalize()
    time.sleep(2)
    print(f"Hi {player_name}!\n")
    time.sleep(2)
    print("OK, let's start the game.\n")
    time.sleep(1)
    intro(player_name)


# function to set scene and start game

def intro(player_name):
    """
    set scene
    start game
    get host name from player for global use

    """
    print("You wake up in an unfamiliar room as dawn is breaking.\n")
    time.sleep(2)
    print("Bit of a headache.\n")
    print("Whose house is this again?\n")
    time.sleep(0.5)
    host_name = (input(f"{player_name} who had the party?\n").capitalize())
    print(f"Oh yes {host_name}'s party - just moved back from abroad...\n")
    print("Great night anyway.")
    print("Good crowd.")
    print("Wonder how many crashed here?")
    time.sleep(2)
    print("Hmmm..probably shouldn't have been partying with that virus"
          " spreading and everything.")
    time.sleep(2)
    print("They say it could be deadly.\n")
    print("You hear some groaning from outside.\n")
    time.sleep(2)
    print("You look out the window.\n")
    time.sleep(1)
    print("There's a couple of people from the party shuffling around"
          " the driveway near your car.\n")
    time.sleep(2)
    print("Must've had too much to drink.\n")
    time.sleep(2)
    print("They don't look at all well.")
    time.sleep(2)
    print("Very pale.\n")
    bedroom(host_name, player_name)


def bedroom(host_name, player_name):
    """
    get friend name from player
    """
    print("You notice the bed is empty.\n")

    # user assigns friend name

    friend_name = input(f"{player_name}, who did you come to the party with?"
                        "\n").capitalize()
    time.sleep(2)
    print("That's weird...\n")
    time.sleep(1)
    print(f"Where has {friend_name} got to??\n")
    time.sleep(2)
    print("Sleepwalking again probably.\n")
    time.sleep(2)
    print("Better head off anyway.")
    time.sleep(1)
    print(f"{friend_name}'s probably downstairs\n")
    print("You pull on your clothes and look around the room.")
    print("Don't remember going to bed at all...")
    time.sleep(2)
    print("Which way out?\n")
    time.sleep(2)
    print("There are two doors in the bedroom."
          "One is on the left and one on the right.")
    time.sleep(1)

    """
    user chooses left or right door
    convert choice to lower case
    if / else statement for door choice to move to bathroom or landing
    """
    door_choice = input("Which do you choose? Left or Right\n")
    if "l".lower() in door_choice:
        print("You chose the door on the left\n")
        time.sleep(2)
        left_bathroom(friend_name)
    elif "r".lower in door_choice:
        print("You chose the door on the right")
        landing(friend_name)
    else:
        print(input("Please enter left or right"))


def left_bathroom(friend_name):
    """
    player is in bathroom
    if statement for player choice to open shower curtain

    """
    print("You open the door.\n")
    time.sleep(2)
    print("Just the bathroom.\n")
    time.sleep(2)
    print("Before you go back out you notice a shape behind the "
          "shower curtain.")
    time.sleep(1)
    print("Did it just move...?")
    time.sleep(1)
    print("What the ...??\n")
    time.sleep(1.5)
    choice = (input("Do you open the curtain? (Yes or No)\n"))
    if "y" in choice:
        print(f"Looks like you found {friend_name} …\n")
        time.sleep(2)
        print(f"except it’s not {friend_name} any more....\n")
        time.sleep(2)
        print("Their skin is rotting and their eyes are white…\n")
        time.sleep(1.5)
        print("AGGGGGGGGHHHHHHHHHH...\n")
        time.sleep(2)
        you_die(f"{friend_name} sinks their teeth into your neck… YOU DIE")
    elif "n" in choice:
        print("You picked no. \n")
        time.sleep(2)
        print("You go back into the bedroom and open the other door")
        landing(friend_name)
        time.sleep(1)
    else:
        print("Please choose yes or no")


# function for user
def landing(friend_name):
    camping_box = [
        "knife", "hammer", "tent peg", "rope", "frying pan", "nail scissors"]
    print("You come out of the bedroom onto the landing\n")
    print("From behind you, you hear a crash and a groan")
    time.sleep(1.5)
    print("Sounds like someone's in the bathroom")
    time.sleep(1)
    print(f"{friend_name}??")
    time.sleep(1.5)
    print(f"You turn around and see {friend_name} staggering towards you.")
    time.sleep(1)
    print("their skin is green and ....rotting...euch...")
    time.sleep(1)
    print("and their eyes... rolling in their sockets")
    time.sleep(1.5)
    print("Their arms are outstretched and it is not for a warm hug "
          "by the looks of it")
    time.sleep(1.5)
    print("Arrrggghh, that virus .... household gatherings .... should have "
          "listened...")
    time.sleep(1.5)
    print("No time to think about that now. Need a weapon")
    time.sleep(1)
    print("You see a cardboard box marked 'camping equipment' "
          "just by the door.\n")
    user_answer = input("What do you do?\n")
    if user_answer.lower() in ["box", "open", "look", "inside", "see"]:
        print("you decided to open the box")
        time.sleep(1)
        print("You open the box.\n")
        print("Inside the box there's a")
        for x in camping_box:
            print(x)
        time.sleep(1.5)
        user_choice = (input("Which item do you grab?\n"))
        print(user_choice)
        inventory.append(user_choice)
        user_choice = (input("Might as well grab one more just in case\n"))
        for x in inventory:
            print(x)

    else:
        input("I really think you should open the box")


def bedroom1():
    print("you are in bedroom1")

# say hi
# if weapon in inventory --> kill --> stairs
# if no weapon -- > window
# if no weapon --> if rope --> win -- > if no rope die

# def stairs():
# hide or attack: if radio die
# if weapon --> downstairs()

# def bedroom_2
# dog attracts zombies
# if rope --- window --> win
# if no rope ---> die

# def living_room
# if weapon get to locked front door
# if tool pick lock --> win

# def kitchen
# host in cupboard with key --> open cupboard win


# function for when user dies and game ends
def you_die(reason):
    print(reason)
    time.sleep(2)
    play_again()


# function to ask user to play game again
def play_again():
    print("\nSorry you didn't make it home from the party.\n")
    time.sleep(2)
    answer = input("Do you want to try again? Yes or No\n")
    if "y" in answer:
        print("Good decision.\nYou can definitely make it out this time!\n")
        time.sleep(1)
        print("Good luck!\n")
        time.sleep(2.5)
        welcome()
    elif "n" in answer:
        print("No worries. Come back soon!")


# def living_room():
#

# def kitchen():
    # print("you are upstairs")

# def downstairs():
    # print("you are downstairs")


# function to start game

welcome()
