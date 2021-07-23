# python module to give delay between lines of text
import time
from title import title
# Empty list to hold weapons and tools selected by player
inventory = []


def welcome():
    """
    Dsplays title
    Welcomes and gets player's name
    """
    title()
    print()
    print("Hello there!")
    time.sleep(1)
    # player enters name
    # While loop checks player_name input is not empty or spaces
    while True:
        global player_name
        player_name = input("What's your name?:\n").capitalize()
        if not player_name:
            print("You can't play if you don't enter a name!")
            continue
        elif player_name.isspace():
            print("You can't play if you don't enter a name!")
            continue
        else:
            break
        time.sleep(1)
    print(f"Hi {player_name}!\n")
    time.sleep(1.5)
    print("OK, let's start the game.\n")
    time.sleep(1)
    intro()


def intro():
    """
    Sets the opening scene
    Get party host's name from player for global use

    """
    print("You wake up in an unfamiliar room as dawn is breaking.")
    time.sleep(1.5)
    print("Bit of a headache.\n")
    time.sleep(1.5)
    print("Great night anyway.")
    time.sleep(1.5)
    print("Good crowd.")
    time.sleep(1.5)
    print("Wonder how many crashed here?\n")
    time.sleep(1.5)
    print("Whose house is this again?")
    time.sleep(1.5)

    # while loop repeats request for valid host_name input if player input is
    # space or empty
    while True:
        global host_name
        host_name = (input(f"{player_name} who was the host of the "
                     "party?\n").capitalize())
        if not host_name:
            print("You can't play if you don't enter a name!")
            continue
        elif host_name.isspace():
            print("You can't play if you don't enter a name!")
            continue
        else:
            break
    print(f"Oh yes {host_name}'s party - just moved back from abroad...\n")
    time.sleep(1.5)
    print("Hmmm..probably shouldn't have been partying with that virus"
          " spreading\nand everything.")
    time.sleep(1.5)
    print("They say it could be deadly.\n")
    time.sleep(1.5)
    print("You hear some groaning from outside.")
    time.sleep(1.5)
    print("You look out the window.")
    time.sleep(1.5)
    print("There's a couple of people from the party shuffling around"
          " the driveway \nnear your car.")
    time.sleep(1.5)
    print("Must've had too much to drink.")
    time.sleep(1.5)
    print("They don't look at all well.")
    time.sleep(1.5)
    print("Very pale.\n")
    time.sleep(1.5)
    bedroom()


def bedroom():
    """
    Gets friend's name from player for global use
    User chooses left or right door
    """
    print("You notice the bed is empty.")
    time.sleep(1.5)

    # user assigns friend name
    # while loop checks for valid text input and repeats if not
    while True:
        global friend_name
        friend_name = input(f"{player_name}, who did you come to the party "
                            "with?\n").capitalize()
        if not friend_name:
            print("You can't play if you don't enter a name!")
            continue
        elif friend_name.isspace():
            print("You can't play if you don't enter a name!")
            continue
        else:
            break
    time.sleep(1)
    print("That's weird...")
    time.sleep(1.5)
    print(f"Where has {friend_name} got to??")
    time.sleep(1.5)
    print("Sleepwalking again probably.")
    time.sleep(1.5)
    print("Better head off anyway.")
    time.sleep(1.5)
    print(f"{friend_name}'s probably downstairs.\n")
    print("You pull on your clothes and look around the room.")
    time.sleep(1.5)
    print("Don't remember going to bed at all...")
    time.sleep(1.5)
    print("Which way out?\n")
    time.sleep(1.5)
    print("There are two doors in the bedroom. "
          "One is on the left and one on the right.")
    time.sleep(0.5)

    # While loop checks for valid user input and repeats question in case of
    # invalid user choice
    # Converts choice to lower case to accept user using capitals
    # If / else statement for door choice to move to bathroom or landing

    while True:
        door_choice = input("Which do you choose? Left or Right\n").lower()
        if door_choice == "left":
            print("You chose the door on the left\n")
            time.sleep(1.5)
            left_bathroom()
            break
        elif door_choice == "right":
            print("You chose the door on the right")
            time.sleep(1.5)
            landing()
            break
        else:
            print(input("Please enter left or right\n"))
            time.sleep(0.5)
            continue


def y_n_check(question):
    """
    function to check if player imputs yes or no
    While loop to repeat prompt in case of user invalid entry
    """
    while True:
        ask_y_n = input(question).lower()
        if ask_y_n == "yes":
            return "yes"
        elif ask_y_n == "no":
            return "no"
        else:
            print("No time to dilly-dally!")
            continue


def left_bathroom():
    """
    Player is in bathroom
    If statement for player choice to open shower curtain

    """
    print("You open the door.")
    time.sleep(1.5)
    print("Just the bathroom.\n")
    time.sleep(1.5)
    print("Before you go back out you notice a shape behind the "
          "shower curtain.")
    time.sleep(1.5)
    print("Did it just move...?")
    time.sleep(1.5)
    print("What the ...??")
    time.sleep(1.5)

    y_or_n = y_n_check("Do you open the curtain? (Yes or No)\n")
    if y_or_n == "yes":
        print("You picked yes\n")
        print(f"Looks like you found {friend_name}...\n")
        time.sleep(1.5)
        print(f"except it’s not {friend_name} any more...\n")
        time.sleep(1.5)
        print("Their skin is rotting and their eyes are white…\n")
        time.sleep(1.5)
        print("AGGGGGGGGHHHHHHHHHH...\n")
        time.sleep(1.5)
        you_die(f"{friend_name} sinks their teeth into your neck… \nYOU DIE")
    elif y_or_n == "no":
        print("You picked no. \n")
        time.sleep(1.5)
        print("You go back into the bedroom and open the other door")
        landing()
        time.sleep(1.5)


def landing():
    """
    User is prompted to suggest opening camping box
    """
    camping_box = [
        'knife', 'hammer', 'rope', 'hairpin', 'peg',
        'screwdriver']
    print("You come out of the bedroom onto the landing\n")
    print("From behind you, you hear a crash and a groan")
    time.sleep(1.5)
    print("Sounds like someone's in the bathroom\n")
    time.sleep(1.5)
    print(f"{friend_name}??\n")
    time.sleep(1.5)
    print(f"You turn around and see {friend_name} staggering towards you.")
    time.sleep(1.5)
    print("Their skin is green and ....rotting...euch...")
    time.sleep(1.5)
    print("and their eyes... rolling in their sockets")
    time.sleep(1.5)
    print("Their arms are outstretched and \nit is not for a warm hug "
          "by the looks of it\n")
    time.sleep(1.5)
    print("ARRRRRGGGGGHHHHH\n")
    print("That virus .... household gatherings .... should have "
          "listened...")
    time.sleep(1.5)
    print("No time to think about that now. Need a weapon\n")
    time.sleep(1.5)
    print("You see a cardboard box marked 'camping equipment' "
          "just by the door.\n")
    time.sleep(1.5)
    print("The box might have something useful in it")
    time.sleep(0.5)
    print("What do you want to do? \n ")

    # while loop repeats prompt in case of invalid user entry
    while True:
        user_answer = input("Type one word!(Hint: open): \n")
        if user_answer.lower(
        ) in [
             "box", "open", "open it", "look", "inside", "look inside", "see"]:
            print("You decided to open the box")
            time.sleep(1.5)
            print("Quickly you tear open the lid.")
            time.sleep(1.5)
            open_camping_box(camping_box)
            break
        else:
            print("Sorry, what did you say? What do you want to do "
                  "with the box??")
            continue


def open_camping_box(camping_box):
    """
    Player selects one weapon/tool from camping box and moves to bedroom
    """
    print("Inside the box there's a:")

    # For loop displays items in camping box list
    for x in camping_box:
        print(x)
        time.sleep(0.2)

    # While loop to check for valid input and repeat prompt if not
    while True:
        time.sleep(1.5)
        user_choice1 = input("\nWhich item do you grab?\n").lower()
        time.sleep(0.5)
        print(f"You picked a {user_choice1}")
        time.sleep(1.5)

        """
        If player choice is valid item is added to inventory list
        and removed from camping box list
        """
        if user_choice1 in camping_box:
            inventory.append(user_choice1)
            camping_box.remove(user_choice1)
            bedroom1(camping_box)
            break
        else:
            print(f"That's not in the box! Be quick, {friend_name} is"
                  " getting closer!")
            time.sleep(1.5)
            continue


def bedroom1(camping_box):
    """
    Player is in bedroom and chooses whether to 'say hi' to couple in bed

    """
    print("There's a door beside you. You open it and run in.\n")
    time.sleep(1.5)
    print("SLAM!!!\n")
    time.sleep(1.5)
    print("Two people in bed. Looks like that couple Erin and Denis.\n")
    time.sleep(1.5)
    print("Could they be ALIVE?\n")
    time.sleep(1.5)

    # If/elif statement for player to choose yes or no
    # If yes player moves to say_hi()
    # If no player moves to landing2()

    y_or_n = y_n_check("Do you say 'Hi'? (Yes or No)\n")
    if y_or_n == "yes":
        print("You picked yes\n")
        say_hi(friend_name, camping_box)
    elif y_or_n == "no":
        print("You picked no. \n")
        landing2(camping_box)
        time.sleep(1.5)


def say_hi(friend_name, camping_box):
    """
    Player chooses whether to fight or run
    If player chooses to fight there are two outcomes.
    If they have the knife is ithey can move on
    If they don't have the knife they die
    If the player chooses not to fight they escape out the window
    """

    print("H..H..H..Hello...??\n")
    time.sleep(1.5)
    print("Are they... ALIVE??\n")
    time.sleep(1.5)
    print("They start to get out of the bed with "
          "that familiar groan and putrid stench.\n")
    time.sleep(1.5)
    print("Is EVERYBODY in this house zombiefied??")
    time.sleep(1.5)

    # while loop allows prompt to be repeated if player entry is invalid
    while True:
        user_answer = input("Do you want to fight or run? (fight/run)\n")
        time.sleep(0.5)
        if user_answer.lower() == "fight":
            print("You are going to fight")
            time.sleep(1.5)
            if "knife" in inventory:
                print("Good thing you picked that from the box! \nNow"
                      " 'stick 'em with the pointy end' as they say.\n ")
                time.sleep(1.5)
                print("You stab Denis between the eyes and green goo pours "
                      "out. ")
                print("\nEuchh. \nDenis falls on top of Erin and she"
                      " is trapped\n")
                time.sleep(1.5)
                print(f"{friend_name} grabs your arm from behind and you swing"
                      " around and jab them in the forehead. More slime.\n")
                time.sleep(1.5)
                print("Quickly. Back out of this room anyway before Erin gets"
                      " out. Have to find a way out\n")
                time.sleep(1.5)
                landing2(camping_box)
                break
            elif "screwdriver" in inventory:
                print("Good thing you picked that from the box! \nNow"
                      " 'stick 'em with the pointy end' as they say.\n ")
                time.sleep(1.5)
                print("You stab Denis between the eyes and green goo pours "
                      "out.\n ")
                print("\nEuchh. \nDenis falls on top of Erin and she"
                      " is trapped\n")
                time.sleep(1.5)
                print(f"{friend_name} grabs your arm from behind and you swing"
                      " around and jab them in the forehead. More slime.\n")
                time.sleep(1.5)
                print("Quickly. Back out of this room anyway before Erin gets"
                      " out. Have to find a way out\n")
                time.sleep(1.5)
                landing2(camping_box)
                break
            elif "hammer" in inventory:
                print("You slam the hammer into Denis's head")
                print(" and his head disintegrates into small pieces of "
                      "bone and strings of goo.")
                time.sleep(1.5)
                print("\nDenis falls on top of Erin and she"
                      " is trapped\n")
                time.sleep(1.5)
                print(f"{friend_name} grabs your arm from behind and you swing"
                      " around and smash her in the \nforehead. More slime.\n")
                time.sleep(1.5)
                print("Quickly. Back out of this room anyway before Erin gets"
                      " out. Have to \nfind a way out")
                time.sleep(1.5)
                landing2(camping_box)
            else:
                you_die("\nYou don't have a weapon! Erin and Denis grab you "
                        "and take chunks of \nflesh out of your face. "
                        "\nYOU DIE\n")
                break
        elif user_answer.lower() == "run":
            print("\nYou don't want to fight. Oh dear. Hope you have a better"
                  " idea.")
            time.sleep(1.5)
            print(f"{friend_name} is coming through the door now...")
            time.sleep(1.5)
            print("\nAnd Erin and Dennis are standing up...\n")
            time.sleep(1.5)
            print("There's no way out....but wait")
            time.sleep(1.5)
            print("There's a window past the bed. You make a run for it")
            time.sleep(1.5)
            print("\nIt's open! (That was lucky!)\n")
            time.sleep(1.5)
            you_win("You shimmy down the drainpipe. You're out. \nYOU WIN!\n")
            break
        else:
            print("Make up your mind!")
            time.sleep(1)
            continue


def landing2(camping_box):
    """
    Player chooses another item from the camping box
    Item is added to player inventory list and removed from camping list
    Player chooses whether or not to open the door to bedroom2
    """

    print("Back out on the landing\n")
    time.sleep(1.5)
    print("Better grab something else from the camping box\n")
    print("Inside the box there's a:")

    # loop through updated camping box list
    for x in camping_box:
        print(x)
    time.sleep(1.5)

    # While loop to check for valid input and repeat prompt if not
    while True:
        user_choice1 = input("\nWhich item do you grab?\n").lower()
        time.sleep(0.5)
        print(f"You picked a {user_choice1}\n")
        if user_choice1 in camping_box:
            inventory.append(user_choice1)
            camping_box.remove(user_choice1)
            break
        else:
            print("That's not in the box! Be quick!")
            continue
    time.sleep(1.5)
    print("You hear thumping footsteps on the stairs. \nOh no... more of those"
          " ...things...people must've crashed downstairs...\n")
    time.sleep(1.5)
    print("You see another door")

    y_or_n = y_n_check("Do you open the door? (Yes or No)\n")
    if y_or_n == "yes":
        print("You picked yes\n")
        bedroom2()
    elif y_or_n == "no":
        print("You picked no. \n")
        time.sleep(1.5)
        print("You turn to the stairs")
        time.sleep(1.5)
        stairs()


def bedroom2():
    """
    Player is offered choice to get out window
    If player says yes and has rope player wins
    If yes without rope player dies
    If no player continues to stairs

    """
    print("You open the door cautiously. Something white flies at you\n")
    time.sleep(1.5)
    print("What the ....!!!\n")
    time.sleep(1.5)
    print(f"Phew, just a dog!! {host_name} said they put their dog upstairs "
          "when \nthe party got crazy. \n"
          "At least there's no dead people anyway.\n")
    time.sleep(1.5)
    print("The dog starts barking\n")
    time.sleep(1.5)
    print("Noooo! Sssshhh!\n")
    time.sleep(1.5)
    print("Too late. You hear more footsteps on the stairs")
    print("What are you going to do?\n")
    time.sleep(1.5)
    print("You look around the room. There's a window.")
    print("Could you get out that way?\n")

    y_or_n = y_n_check("Do you want to try the window? (Yes or No?)\n")
    if y_or_n == "yes":
        if "rope" in inventory:
            you_win("\nYou tie the rope around the window handle and climb"
                    "  down. \n(And the dog jumps down into your arms!)"
                    " \nDouble WIN!!")
        else:
            you_die("You're not a rubber ball!! You jump out the window "
                    "and break your neck. \nYOU DIE!!")
    elif y_or_n == "no":
        print("Hope you've got a weapon then.")
        time.sleep(1.5)
        stairs()


def stairs():
    """
    Player is asked to choose yes or no to fight
    If yes player proceeds downstairs
    If no player dies
    """
    print("You are on the stairs")
    time.sleep(1.5)
    print("Dead party-goers are trooping up the stairs.\nThe first one is"
          " at the top\n")
    time.sleep(1.5)

    y_or_n = y_n_check("Are you going to attack? (Yes or No)\n")
    if y_or_n == "yes":
        print("You're going to attack...\n")
        if "hammer" in inventory:
            time.sleep(1.5)
            print("You smash the hammer into its head and slime"
                  " and skull splat everywhere.\n")
            time.sleep(1.5)
        elif "knife" in inventory:
            time.sleep(1.5)
            print("You knife it in the forehead and slime and"
                  " skull splat everywhere.\n")
            time.sleep(1.5)
        elif "screwdriver" in inventory:
            time.sleep(1.5)
            print("You ram the screwdriver through its eye and"
                  " slime and skull splat everywhere.\n")
            time.sleep(1.5)
        else:
            time.sleep(1.5)
            print("You give it a good hard shove.\n")
        print("Good job! It falls back and the rest topple down "
              "like dominoes. \nYou climb over the pile of"
              " bodies and reach the bottom \nof the stairs.\n")
        living_room()
    elif y_or_n == "no":
        print("You picked no. \n")
        time.sleep(1.5)
        you_die("There's no escape. The horde swarms up the stairs"
                " and it ain't pretty. \nYOU DIE\n")


def living_room():
    """
    Player chooses yes/no whether to fight or not
    If yes and suitable weapon player reaches front door
    If no weapon player dies
    If chooses no player dies
    """

    print("You are in the living room and can see the front door")
    time.sleep(1.5)
    print("But the way is blocked by a good dozen dead creatures")
    time.sleep(1.5)
    print("They haven't seen you yet.")
    time.sleep(1.5)
    print("How to get through...\n")
    time.sleep(1.5)

    def output():
        print("You battle your way bravely with your last "
              "drop of energy and clear a path.\n")
        time.sleep(1.5)
        print("You reach the front door")
        time.sleep(1.5)
        print("Thank the lord!!\n")
        time.sleep(1.5)
        print("But wait...it's LOCKED????")
        time.sleep(1.5)
        print("Where the hell is the key???")
        time.sleep(1.5)
        front_door()
    y_or_n = y_n_check("Do you have the energy to fight your way "
                       "through? (Yes or No)\n")
    if y_or_n == "yes":
        print("You picked yes\n")
        if "hammer" in inventory:
            output()
        elif "knife" in inventory:
            output()
        elif "screwdriver" in inventory:
            output()
        else:
            you_die("You can't get through them without a good weapon!")
    elif y_or_n == "no":
        print("You picked no. \n")
        time.sleep(1.5)
        you_die("The dead turn towards you. You turn to go back up. "
                "\nBut Erin is coming down the stairs."
                "There's no escape. Sorry \nYOU DIE")


def front_door():
    """
    Player prompted yes/no to pick lock
    If yes and hairpin/screwdriver player wins
    If no player chooses yes/no to enter cupboard
    If no player dies

    """
    print("I don't believe it... what used to be Erin is coming across "
          "the living \nroom now. \nShould have finished her off "
          "upstairs.\nAnd she is followed by more from the stairs."
          " Got to get out quick!!! ")
    time.sleep(1.5)
    y_or_n = y_n_check("Do you want to try to pick the lock?\n")
    if y_or_n == "yes":
        if "hairpin" in inventory:
            you_win("You pick the lock with the hairpin. \nYou burst through  "
                    "the door into the sunlight and speed away in your car. "
                    "YOU WIN!")
        elif "screwdriver" in inventory:
            you_win("You unscrew the lock. You burst through the door "
                    "to the safety of your car and speed off. \nYOU WIN ")
        else:
            you_die("What a shame...you don't have a tool for that! "
                    "Erin and friends grab you by the hair and take "
                    "chunks out of your skull. \nYOU DIE")
    elif y_or_n == "no":
        print("You're out of energy and ideas.")
        time.sleep(1.5)
        print("Maybe a rest will help before you tackle the rest "
              "of the dead")
        time.sleep(1.5)
        print("There's a cupboard over there. With a latch on the outside")
        y_or_n = y_n_check("You could rest in there. Do you open it? "
                           "Yes or No?\n")
        if y_or_n == "yes":
            print("You picked yes\n")
            time.sleep(1.5)
            cupboard()
        elif y_or_n == "no":
            you_die("There's no escape then. All hope is lost. You "
                    "become Erin's next feast. \nYOU DIE")


def cupboard():
    """
    In this function the player wins
    """
    print(f"You lift the latch and a voice says '{player_name}??'")
    time.sleep(1.5)
    print(f"'{host_name}?'")
    time.sleep(1.5)
    you_win(f"{host_name} has the key to the from door! "
            "You race over and open the door. You both speed "
            "off to safety. \nYOU WIN!\n")


def you_win(reason):
    """
    Function to give reason why player wins
    """
    print(reason)
    time.sleep(2)
    play_again()


def you_die(reason):
    """
    function for when user dies and game ends
    """
    print(reason)
    time.sleep(2)
    print()
    play_again()


# function to ask user to play game again
def play_again():
    """
    function to ask if player wants to play again
    If player inputs yes game restarts
    """

    y_or_n = y_n_check("Do you want to play again?\nYes or No?\n")
    if y_or_n == "yes":
        print("You picked yes\n")
        print("Great!\n")
        time.sleep(1)
        print("Good luck!\n")
        time.sleep(1.5)
        welcome()
    elif y_or_n == "no":
        print("No worries. Come back soon!")
    # answer = input("Do you want to play again? (Yes or No)\n")
    # if "y".lower() in answer:
    #     print("Great!\n")
    #     time.sleep(1)
    #     print("Good luck!\n")
    #     time.sleep(2.5)
    #     welcome()
    # elif "n".lower() in answer:
    #     print("No worries. Come back soon!")


# function to start game
# welcome()
play_again()

