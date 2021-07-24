# After the Party
After the Party Live Link [here](https://after-the-party.herokuapp.com/)
Mockup:

![alt-text](assets/images/responsive.png)


## Overview
After the Party is a lighthearted zombie escape game which runs in a mock terminal on Heroku. The player wakes up after a party in an unfamiliar house where everyone else seems to have turned into zombies. 

## How to Play
After the Party is a text-based adventure game where the player is inputs their answers based on choices prompted in order to navigate their way around the house trying to get out safely. The player chooses Yes/No to open doors to different rooms, turn left/right, attack/run. The player also selects items from a box which help to win the game. There may be red herrings in the box so choose carefully! There may also be unexpected ways to win!

## Features
### Existing Features
### Run After the Party button
This button starts or restarts the programme.

![alt-text](assets/images/run_button.png)


* The game opens with the title and welcome followed by a request for the player to imput their name.

The opening screen of the program showing the title and the player's first input which is their player name:

![alt-text](assets/images/screen1.png)


* The player chooses the name of the party host and the friend they came to the party with. These people then appear later in the story. This is intended to be a source of amusement to engage the user. All three name inputs (Player, Host and Friend) must be in valid text form and cannot be a space or empty or characters other than text. If the player enters a lower case first letter for the name this is accepted and converted to a capital first letter to be grammatically correct. A name must be entered to continue.


![alt-text](assets/images/screen6.png)


Name converts to initial capital letter:

![alt-text](assets/images/screen9.png)


Incorrect name entered:


![alt-text](assets/images/screen8.png)





* The player chooses items from a camping box, most of which then assist in winning the game in various different ways. The player must choose a valid item from the box to continue. The player can choose a second item from the box at a later point and the first item has been removed from the choice offered.

This shows the player choosing to 'open' the camping box. They could also 'look' or 'see' inside the box. The contents list is displayed from which the player selects an item. The programme then confirms the player's choice and continues the story path:


![alt-text](assets/images/screen2.png)


Further on in the game the player chooses another item from the box where the original has been removed as shown here:


![alt-text](assets/images/screen5.png)


* The different rooms the player enters have different paths to win or lose according to their answer choices. 
This shows the player choosing to open the door and finding themselves in the bathroom:

![alt-text](assets/images/screen7.png)


* Winning is escaping from the house and losing is dying or being killed. The means of winning or losing is told to the player at the end of the game.

This shows one way that a player could win.


![alt-text](assets/images/screen3.png)


This screenshot shows one way that a player has died.


![alt-text](assets/images/screen4.png)


### Future Features
* The yes/no questions were refactored into one helper function as they were the majority of the input options. In the future the functions to check the validity of the three names. Currently the player is prevented from entering an empty string or a space and is not able to continue without enterring valid text. This would be done in by calling one function for all names.
* More rooms, more weapons/tools and more scenarios for escaping/dying using the different weapons/tools could be added to extend the experience.
* Ascii art could be added to enhance user experience in particular for the 'You Win' and 'You Die' messages.

### Program Structure
The flowchart created during the planning stage can be viewed [here](https://github.com/siobhanlgorman/After-the-Party/blob/main/assets/images/flowchart.png). 

![alt-text](assets/images/flowchart.png)

## Technologies
### Languages.. 
* [Python](https://www.python.org/) is an interpreted, object-oriented, versatile and powerful programming language used for example for web development, machine learning and data science. Python3 was used to create the command line interface for this text-based game.
### Other Technologies and Libraries
* [Github](https://github.com/) and [Git](https://git-scm.com/) were used for version control. Github provides the web interface for the Git code repository.
* [Gitpod](https://gitpod.io/) was used as the cloud-based IDE for this project.
* [Heroku](http://heroku.com/) is a containier-based cloud Platform as a service used to deploy, manage and scale modern applications. Heroku was used to deploy this game application.
* [The Google Chrome browser](https://www.google.com/intl/en_ie/chrome/) was used to view the app
* [Diagrams](https://www.diagrams.net/) was used to create the flowchart for this application.
## Known Issues/Bugs
* Left/Right option: sometimes won't accept 'Right' or 'right' input but accepts second time and sometimes it accepts first time as expected. The cause has not been determined as is intermttent so a fix cannot be identified currently. Update: Fixed - removed additional input from `else` statement in `while` loop.

Not accepting 'right':

![alt-text](assets/images/error2.png)

Accepting 'right':

![alt-text](assets/images/error2not.png)

* Player was able to continue with game after hitting return instead of entering a valid player name. This was fixed with a while loop and `if not player_name:`. But the player was still able to enter spaces. I experimented with several ways but eventually fixed this by adding an elif statement and the `isspace()` method. In the end to eliminate player inputting e.g.??? I changed this to the `isalpha()` method.

* In the landing function user answer is incorrect if more than one word entered which is not in list of accepted words or strings e.g 'I would open it' instead of just open so added prompt 'enter one word (hint: open)'. This could be changed in the future if it proved to be problematic for users I would change the function but wanted a little variety and to allow the user a little freer choice. Testers have no problem with this.

## Testing
### Validation
Validation of the Python code was carried out by [PEP8](http://pep8online.com/). No errors were found.
![alt-text](assets/images/pep8.png)


### Manual Testing
1. Manual testing was carried out extensively both in the terminal and also in the browser. Once testing in the browser was conducted a lot of additional line breaks were needed to compensate for the width of the screen.
2. The options and flow were checked manually and all passed. The list of these tests can be seen [here:](https://docs.google.com/spreadsheets/d/1NUVHJ0VQ0orWFZ3Bh9MgGXAYShW9a5Ki2Rw6T_ssCLE/edit?usp=sharing)


![alt-text](assets/images/test_sheet.png)


3. In testing some users had difficulty with the prompt to open the box in the landing function so I added a "hint: open" to the text to avoid frustration
4. In testing it was apparent that a player could enter a space or hit return to enter a player name and still continue. To prevent this I added a function checking for a name and only space (`str.isspace()`) But this allowed the player to enter e.g. 555 or ??? so I changed the method to `str.isalpha`. It is recognised however that were a player to have a squiggle or other novel element in their name (like the artist formerly known as Prince did) they would not be able to enter this. If this was proven to be an issue it could be addressed in future versions of the game. 
5. The game was tested on various sized screens and browsers including a Dell 15" laptop, 24" monitor, iPhone SE2 and Moto G8+ with no issues.


IPhoneSE2:

![alt-text](assets/images/iphone_se2_1.jpg)


![alt-text](assets/images/iphone_se2_2.jpg)

Moto G8+:

![alt-text](assets/images/motog8.png)

## Deployment
This application uses Heroku for deployment

### To create the application:
1. First create the requirements file the Heroku will use to import the dependencies required for deployment: type `pip3 freeze > requirements.txt`. For this project the requirements.txt file is empty as no libraries or modules were imported other than from the standard python library.
2. Navigate to the [Heroku](https://www.heroku.com/) website
3. create an account by entering your email address and a password
4. Activate the account through the authentication email sent to your email account
5. Click the new button and select create a new app from the dropdown menu
6. Enter a name for the application which must be unique, in this case the app name is after-the-party
7. Select a region, in this case Europe
8. Click create app

### Heroku settings
1. From the horizontal menu bar select 'Settings'.
2. In the buildpacks section, where further necessary dependencies are installed, click 'add buildpack'. Select 'Python' first and click 'save changes'. Next click 'node.js' and then click 'save changes' again. The 'Python' buildpack must be above the 'node.js' buildpack'. They can be clicked on and dragged to change the order if necessary.
### Deployment
1. In the top menu bar select 'Deploy'.
2. In the 'Deployment method' section select 'Github' and click the connect to Github button to confirm.
3. In the 'search' box enter the Github repository name for the project. Click search and then click connect to link the heroku app with the Github repository. The box will confirm that heroku is connected to the repository which in this case is [After the Party](https://github.com/siobhanlgorman/After-the-Party).
4. Scroll down to select either automatic or manual deployment. For this project automatic deployment was selected. If you wish to select automatic deployment select the button 'Enable Automatic Deploys'. This will rebuild the app every time a change is pushed to Github. If you wish to manually deploy click the button 'Deploy Branch'. The default 'Master' option in the dropdown menu should be selected in both cases.
5. When the app is deployed a message 'Your app was successfully deployed' will be shown. Click 'view' to see the deployed app in the browser. The live deployment of the project can be seen [here](https://after-the-party.herokuapp.com/)
6. The app starts automatically and can be restarted by pressing the 'Run Program' button.
### Forking the Repository
If you wish to fork the repository to make changes without affecting the original you can fork the repository
1. Navigate to the [After the Party repository](https://github.com/siobhanlgorman/After-the-Party)
2. Click the 'Fork' button at the top right of the page.
3. A forked copy of the repository will appear in your Repositories page.
### Cloning the Repository
1. On [GitHub](https://github.com/siobhanlgorman/After-the-Party) navigate to the main page of the repository.
2. Above the list of files click the dropdown code menu.
3. Select the https option and copy the link.
4. Open the terminal.
5. Change the current working directory to the desired destination location.
6. Type the git clone command with the copied URL: `git clone https://github.com/siobhanlgorman/After-the-Party.git`.
7. Press enter to create the local clone.


## Credits

### Code

This tutorial was useful for inspiration: [Learn Python by making a text-based adventure game](https://coding-grace-guide.readthedocs.io/en/latest/guide/lessonplans/beginners-python-text-based-adventure.html)

[Stack Overflow](https://stackoverflow.com/) was useful for looking up various solutions to bugs e.g. [whitespace only strings](https://stackoverflow.com/questions/2405292/check-if-string-contains-only-whitespace)
## Content
The story content was developed by this author [Siobhan Gorman](https://github.com/siobhanlgorman).