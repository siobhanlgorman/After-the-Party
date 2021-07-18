import time

# Empty list to hold weapons and tools selected by player
inventory = []


def welcome():
    """
    welcome and get user's name
    """
    print("Hello there!")
    time.sleep(1)
    global player_name
    player_name = input("What's your name?:\n").capitalize()
    time.sleep(1)
    print(f"Hi {player_name}!\n")
    time.sleep(1.5)
    print("OK, let's start the game.\n")
    time.sleep(1)
    intro()


# function to set scene and start game

def intro():
    """
    set scene
    start game
    get host name from player for global use

    """
    print("You wake up in an unfamiliar room as dawn is breaking.\n")
    time.sleep(1.5)
    print("Bit of a headache.\n")
    time.sleep(1.5)
    print("Great night anyway.")
    time.sleep(1.5)
    print("Good crowd.")
    time.sleep(1.5)
    print("Wonder how many crashed here?\n")
    time.sleep(1.5)
    print("Whose house is this again?\n")
    time.sleep(1.5)
    global host_name
    host_name = (input(f"{player_name} who was the host of the "
                 "party?\n").capitalize())
    print(f"Oh yes {host_name}'s party - just moved back from abroad...\n")
    time.sleep(1.5)
    print("Hmmm..probably shouldn't have been partying with that virus"
          " spreading\n and everything.")
    time.sleep(1.5)
    print("They say it could be deadly.\n")
    time.sleep(1.5)
    print("You hear some groaning from outside.\n")
    time.sleep(1.5)
    print("You look out the window.\n")
    time.sleep(1.5)
    print("There's a couple of people from the party shuffling around"
          " the driveway \nnear your car.\n")
    time.sleep(1.5)
    print("Must've had too much to drink.\n")
    time.sleep(1.5)
    print("They don't look at all well.")
    time.sleep(1.5)
    print("Very pale.\n")
    time.sleep(1.5)
    bedroom()


def bedroom():
    """
    get friend name from player
    """
    print("You notice the bed is empty.\n")

    # user assigns friend name
    global friend_name
    friend_name = input(f"{player_name}, who did you come to the party with?"
                        "\n").capitalize()
    time.sleep(1.5)
    print("That's weird...\n")
    time.sleep(1.5)
    print(f"Where has {friend_name} got to??\n")
    time.sleep(1.5)
    print("Sleepwalking again probably.\n")
    time.sleep(1.5)
    print("Better head off anyway.")
    time.sleep(1.5)
    print(f"{friend_name}'s probably downstairs\n")
    print("You pull on your clothes and look around the room.")
    time.sleep(1.5)
    print("Don't remember going to bed at all...")
    time.sleep(1.5)
    print("Which way out?\n")
    time.sleep(1.5)
    print("There are two doors in the bedroom. "
          "One is on the left and one on the right.")
    time.sleep(0.5)

    """
    user chooses left or right door
    convert choice to lower case
    if / else statement for door choice to move to bathroom or landing
    """
    while True:
        door_choice = input("Which do you choose? Left or Right\n")
        if "l".lower() in door_choice:
            print("You chose the door on the left\n")
            time.sleep(1.5)
            left_bathroom()
            break
        elif "r".lower() in door_choice:
            print("You chose the door on the right")
            time.sleep(1.5)
            landing()
            break
        else:
            print(input("Please enter left or right\n"))
            time.sleep(0.5)
            continue


def left_bathroom():
    """
    player is in bathroom
    if statement for player choice to open shower curtain

    """
    print("You open the door.\n")
    time.sleep(1.5)
    print("Just the bathroom.\n")
    time.sleep(1.5)
    print("Before you go back out you notice a shape behind the "
          "shower curtain.")
    time.sleep(1.5)
    print("Did it just move...?")
    time.sleep(1.5)
    print("What the ...??\n")
    time.sleep(1.5)
    while True:
        choice = (input("Do you open the curtain? (Yes or No)\n"))
        if "y" in choice.lower():
            print(f"Looks like you found {friend_name} …\n")
            time.sleep(1.5)
            print(f"except it’s not {friend_name} any more....\n")
            time.sleep(1.5)
            print("Their skin is rotting and their eyes are white…\n")
            time.sleep(1.5)
            print("AGGGGGGGGHHHHHHHHHH...\n")
            time.sleep(1.5)
            you_die(f"{friend_name} sinks their teeth into your neck… YOU DIE")
            break
        elif "n" in choice.lower():
            print("You picked no. \n")
            time.sleep(1.5)
            print("You go back into the bedroom and open the other door")
            landing()
            time.sleep(1.5)
            break
        else:
            print("What was that? If you're lazy you can enter y or n!")
            continue


# function for user
def landing():
    camping_box = [
        "knife", "hammer", "rope", "nail scissors", "screwdriver"]
    print("You come out of the bedroom onto the landing\n")
    print("From behind you, you hear a crash and a groan")
    time.sleep(1.5)
    print("Sounds like someone's in the bathroom")
    time.sleep(1.5)
    print(f"{friend_name}??")
    time.sleep(1.5)
    print(f"You turn around and see {friend_name} staggering towards you.")
    time.sleep(1.5)
    print("Their skin is green and ....rotting...euch...")
    time.sleep(1.5)
    print("and their eyes... rolling in their sockets")
    time.sleep(1.5)
    print("Their arms are outstretched and it is not for a warm hug "
          "by the looks of it")
    time.sleep(1.5)
    print("Arrrggghh, that virus .... household gatherings .... should have "
          "listened...")
    time.sleep(1.5)
    print("No time to think about that now. Need a weapon")
    time.sleep(1.5)
    print("You see a cardboard box marked 'camping equipment' "
          "just by the door.\n")
    time.sleep(1.5)
    print("The box might have something useful in it")
    time.sleep(0.5)
    print("What do you want to do? \n ")
    while True:
        user_answer = input("Type one word!: \n")
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
    print("Inside the box there's a:")
    for x in camping_box:
        print(x)
        time.sleep(0.2)
    while True:
        time.sleep(1.5)
        user_choice1 = input("\nWhich item do you grab?\n").lower()
        time.sleep(0.5)
        print(f"You picked a {user_choice1}")
        time.sleep(1.5)
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
    print("There's a door beside you. You open it and run in")
    time.sleep(1.5)
    print("SLAM")
    time.sleep(1.5)
    print("Two people in bed. Looks like that couple Erin and Denis\n")
    time.sleep(1.5)
    print("Could they be ALIVE?")
    time.sleep(1.5)
    while True:
        user_answer = input("Do you say Hi? (Yes or No)\n")
        if "y".lower() in user_answer:
            time.sleep(0.5)
            print("You picked yes")
            say_hi(friend_name, camping_box)
            break
        elif "n".lower() in user_answer:
            time.sleep(0.5)
            print("You picked no")
            landing2(camping_box)
            break
        else:
            print("Better choose quickly the door handle's turning...")
            continue


def say_hi(friend_name, camping_box):
    """
    function for player to choose whether to fight or not
    if player chooses to fight there are two outcomes.
    if they have the knife is ithey can move on
    if they don't have the knife they die
    if the player chooses not to fight they escape out the window
    """

    print("Hello...??\n")
    time.sleep(1.5)
    print(" Are they... ALIVE??\n")
    time.sleep(1.5)
    print("They start to get out of the bed with "
          "that familiar groan and putrid stench.")
    time.sleep(1.5)
    print("Is everybody in this house zombiefied??")
    time.sleep(1.5)
    while True:
        user_answer = input("Do you want to fight? (Yes or No)\n")
        time.sleep(0.5)
        if "y".lower() in user_answer:
            print("You want to fight")
            time.sleep(1.5)
            if "knife" or "screwdriver" in inventory:
                print("Good thing you picked that from the box!\nNow"
                      " 'stick 'em with the pointy end' as they say. ")
                time.sleep(1.5)
                print("You stab Denis between the eyes and green goo pours "
                      "out. \nEuchh. \nDenis falls on top of Erin and she"
                      " is trapped")
                time.sleep(1.5)
                print(f"{friend_name} grabs your arm from behind and you swing"
                      " around and jab them in the forehead. More slime.")
                time.sleep(1.5)
                print("Quickly. Back out of this room anyway before Erin gets"
                      " out. Have to find a way out")
                time.sleep(1.5)
                landing2(camping_box)
                break
            elif "hammer" in inventory:
                print("You slam the hammer into Denis's head")
                print(" and his head disintegrates into small pieces of "
                      "bone and strings of goo.")
                time.sleep(1.5)
                print("\nDenis falls on top of Erin and she"
                      " is trapped")
                time.sleep(1.5)
                print(f"{friend_name} grabs your arm from behind and you swing"
                      " around and smash her in the forehead. More slime.")
                time.sleep(1.5)
                print("Quickly. Back out of this room anyway before Erin gets"
                      " out. Have to find a way out")
                time.sleep(1.5)
                landing2(camping_box)
            else:
                you_die("You don't have a weapon! Erin and Denis grab you and"
                        " take chunks of flesh out of your face. YOU DIE")
                break
        elif "n".lower() in user_answer:
            print("You don't want to fight. Oh dear. Hope you have a better"
                  " idea.")
            time.sleep(1.5)
            print(f"{friend_name} is coming through the door now...")
            time.sleep(1.5)
            print("And Erin and Dennis are standing up...")
            time.sleep(1.5)
            print("There's no way out....but wait")
            time.sleep(1.5)
            print("There's a window past the bed. You make a run for it")
            time.sleep(1.5)
            print("It's open! (That was lucky!")
            time.sleep(1.5)
            you_win("You shimmy down the drainpipe. You're out. YOU WIN!")
            break
        else:
            print("Make up your mind!")
            time.sleep(1)
            continue


def landing2(camping_box):
    """
    """

    print("Back out on the landing")
    time.sleep(1.5)
    print("Better grab something else from the camping box")
    print("Inside the box there's a:")
    for x in camping_box:
        print(x)
    time.sleep(1.5)
    while True:
        user_choice1 = input("\nWhich item do you grab?\n").lower()
        time.sleep(0.5)
        print(f"You picked a {user_choice1}")
        if user_choice1 in camping_box:
            inventory.append(user_choice1)
            camping_box.remove(user_choice1)
            break
        else:
            print("That's not in the box! Be quick!")
            continue
    time.sleep(1.5)
    print("You hear thumping footsteps on the stairs. \nOh no... more of those"
          " things..people must've crashed downstairs...")
    time.sleep(1.5)
    print("You see another door")
    while True:
        time.sleep(0.5)
        user_choice = input("Do you open the door? (Yes or No)\n")
        if "y".lower() in user_choice:
            time.sleep(0.5)
            print("you picked yes")
            bedroom2()
            break
        elif "n".lower() in user_choice:
            time.sleep(0.5)
            print("you picked no")
            time.sleep(1.5)
            print("You turn to the stairs")
            time.sleep(1.5)
            stairs()
            break
        else:
            continue


def bedroom2():
    print("You open the door cautiously. Something white flies at you")
    time.sleep(1.5)
    print("What the ....!!!")
    time.sleep(1.5)
    print(f"Phew, just a dog!! {host_name} said he put his dog upstairs "
          "when the party got crazy. \n"
          "At least there's no dead people anyway.")
    time.sleep(1.5)
    print("The dog starts barking")
    time.sleep(1.5)
    print("Noooo! Sssshhh!")
    time.sleep(1.5)
    print("Too late. You hear more footsteps on the stairs")
    print("What are you going to do?")
    time.sleep(1.5)
    print("You look around the room. There's a window.")
    print("Could you get out that way?")
    time.sleep(1.5)
    while True:
        user_choice = input("Do you want to try the window? (Yes or No?)\n")
        time.sleep(1.5)
        if "y".lower() in user_choice:
            if "rope" in inventory:
                you_win("You tie the rope around the window handle and climb"
                        "  down. (And the dog jumps down into your arms!)"
                        " Double WIN")
                break
            else:
                you_die("You're not a rubber ball!! You jump out the window "
                        "and break your neck")
                break
        elif "n".lower() in user_choice:
            print("Hope you've got a weapon then.")
            time.sleep(1.5)
            stairs()
            break
        else:
            print("Well? Which is it?")
            continue


def stairs():
    print("You are on the stairs")
    time.sleep(1.5)
    print("Dead party-goers are trooping up the stairs.\nThe first one is"
          " at the top")
    time.sleep(1.5)
    while True:
        user_choice = input("Are you going to attack?\n")
        if "y".lower() in user_choice:
            print("You're going to attack")
            output = ("Good job! It falls back and the rest topple down "
                      "like dominoes. You climb over the pile of"
                      " bodies and reach the bottom of the stairs.")
            if "hammer" in inventory:
                time.sleep(1.5)
                print("You smash the hammer into its head and slime"
                      " and skull splat everywhere.")
                time.sleep(1.5)
                print(output)
                living_room()
                break
            elif "knife" in inventory:
                time.sleep(1.5)
                print("You knife it in the forehead and slime and"
                      " skull splat everywhere.")
                time.sleep(1.5)
                print(output)
                living_room()
            elif "screwdriver" in inventory:
                time.sleep(1.5)
                print("You ram the screwdriver through its eye and"
                      " slime and skull splat everywhere.")
                time.sleep(1.5)
                print(output)
                living_room()
            else:
                time.sleep(1.5)
                print("You give it a good hard shove.")
                print(output)
                living_room()
            break
        elif "n".lower() in user_choice:
            time.sleep(1.5)
            you_die("There's no escape. The horde swarms up the stairs"
                    " and it ain't pretty. YOU DIE")
            break
        else:
            print("Better be quick!")
            continue


def living_room():
    print("you are in the living room and can see the front door")
    time.sleep(1.5)
    print("But the way is blocked by a good dozen dead creatures")
    print("They haven't seen you yet.")
    time.sleep(1.5)
    print("How to get through...")
    time.sleep(1.5)

    while True:
        user_choice = input("Do you have the energy to fight your way "
                            "through? (Yes or No)\n")
        time.sleep(1.5)
        if "y".lower() in user_choice:
            print("attack with weapon")
            if "hammer" or "knife" or "screwdriver" in inventory:
                print("You battle your way bravely with your last "
                      "drop of energy and clear a path.")
                time.sleep(1.5)
                print("You reach the front door")
                time.sleep(1.5)
                print("Thank the lord!!")
                time.sleep(1.5)
                print("But wait...it's LOCKED????")
                time.sleep(1.5)
                print("Where the hell is the key???")
                time.sleep(1.5)
                front_door()
            break
        elif "n".lower() in user_choice:
            time.sleep(1.5)
            you_die("The dead turn towards you. You turn to go back up. "
                    "But Erin is coming down the stairs."
                    "There's no escape. Sorry YOU DIE")
            break
        else:
            time.sleep(0.5)
            print("Well, which is it to be?")
            continue


def front_door():
    print("I don't believe it... what used to be Erin is coming across "
          "the living room now. Should have finished her off upstairs.")
    time.sleep(1.5)
    print("Do you have anything to open a locked door?")
    time.sleep(1.5)
    if "screwdriver" in inventory:
        you_win("You pick the lock. You burst through the door "
                "into the sunlight and speed away in your car. YOU WIN ")
    elif "nail scissors" in inventory:
        you_win("You unscrew the lock. You burst through the door "
                "to the safety of your car and speed off. YOU WIN ")
    else:
        while True:
            print("You're out of energy and ideas.")
            time.sleep(1.5)
            print("Maybe a rest will help before you tackle the rest "
                  "of the dead")
            time.sleep(1.5)
            print("There's a cupboard over there. With a latch on the outside")
            user_choice = input("You could rest in there. Do you open it? "
                                "Yes or No?\n")
            if "y".lower() in user_choice:
                time.sleep(1.5)
                print(f"You lift the latch and a voice says '{player_name}??'")
                time.sleep(1.5)
                print(f"{host_name}?")
                time.sleep(1.5)
                you_win(f"{host_name} has the key to the from door! "
                        "You race over and open the door. You both speed "
                        "off to safety. YOU WIN!")
                break
            elif "n".lower in user_choice:
                you_die("So close....and yet so far. Erin reaches you and"
                        "before you can strike she bites off your hand.."
                        "YOU DIE")
                break
            else:
                print("Better decide fast!")
                continue


def you_win(reason):
    print(reason)
    time.sleep(2)
    play_again()


# function for when user dies and game ends
def you_die(reason):
    print(reason)
    time.sleep(2)
    play_again()


# function to ask user to play game again
def play_again():
    answer = input("Do you want to play again? Yes or No\n")
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
