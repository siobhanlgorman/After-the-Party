# introduces game and greet user by name
def intro():
    print("Hello there\n")
    player_name = input("What's your name?\n")
    print(f"Hi {player_name}!")



# set scene

def bedroom():
    print("You wake up in an unfamiliar room as dawn is breaking.\n Bit of a headache.\n Whose house is this again? \n Great party last night though.\n")
    friend_name = input("Who did you come to the party with again?\n")
    print(f"Oh yes ... {friend_name}")
    print("You stretch.\n Probably shouldn't have gone to the party what with that virus spreading and everything. \n Sure it'll never reach us here ")
    print(f"Where the hell is {friend_name} anyway?\n")
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
                print(f"Looks like you found friend_name…except it’s not friend_name any more....AGGGGHHHHHHH... Their skin is rotting and their eyes are white… they sink their teeth into your neck… YOU DIE")
            elif choice == "no":
                print("You picked no")
            else:
                print("Please choose yes or no")
    


#def bathroom():

#def bedroom_1():

#def camping_box():

#def upstairs():

#def downstairs():


def run_game():
    intro()
    bedroom()

run_game()
