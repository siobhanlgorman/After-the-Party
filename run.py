#introduces game and greet user by name
def intro():
    print("Hello there\n")
    player_name = input("What's your name?\n")
    print(f"Hi {player_name}!")

#set scene
def bedroom():
    print("You wake up in an unfamiliar room as dawn is breaking.\n Bit of a headache.\n Whose house is this again? \n Great party last night though.\n")
    friend_name = input("Who did you come to the party with again?\n")
    print(f"Oh yes ... {friend_name}")
    print("You stretch.\n Probably shouldn't have had the party what with that virus spreading and everything. \n Sure it'll never reach us here ")
    print(f"Where the hell is {friend_name} anyway?\n")
    print("You hear some groaning from outside. You look out the window and see a couple of people from the party shuffling around the driveway near your car.\n Must've had too much to drink")
    print("Better head off anyway.\n You pull on your clothes and grab ONE of the following items")

    

#def bathroom():

#def bedroom_1():


def run_game():
    intro()
    bedroom()

run_game()
