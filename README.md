# After the Party
After the Party Live Link [here](https://after-the-party.herokuapp.com/)
## Overview
After the Party is a lighthearted zombie escape game. The player wakes up after a party in an unfamiliar house where everyone else seems to have turned into zombies.You wake up make your way etc
## Features
### Existing Features
player makes choices chooses who to bring etc chooses own path explain different paths explore rooms be careful mighte end up dying etc
### Future Features
Create one function to check the validity of the three names inputted by user

### Run Program button
### Terminal Area
The first screen of the program showingthe opening and the first two player inputs of their player name and the part host name/:
![alt-text](assets/images/screen1.png)

![alt-text](assets/images/screen2.png)
### Program Structure
The flowchart created during the planning stage can be viewed [here](https://github.com/siobhanlgorman/After-the-Party/blob/main/assets/images/flowchart.png)

![alt-text](assets/images/flowchart.png)

## Technologies
### Languages.. 
  * [Python](https://www.python.org/) summary of python goes here
### Other Technologies and Libraries
* [Github](https://github.com/) and [Git](https://git-scm.com/) were used for version control
* [Gitpod](https://gitpod.io/) was used as cloud-based IDE
* [Heroku](http://heroku.com/) was used to deploy the app
* [The Google Chrome browser](https://www.google.com/intl/en_ie/chrome/) was used to view the app
## Known Issues/Bugs
* left/right bug? sometimes won't accept 'Left' input but accepts second time and sometimes accepts. Not sure what's going on
Sometimes won't accept capital L for left but then will. No known fix as usually works
* Player was able to continue with game after hitting return instead of entering a valid player name. This I fixed with a while loop and `if not player_name:`. But the player was still able to enter spaces. I experimented with several ways but eventually fixed this by adding an elif statement and the `isspace()` method.

  * in landing function user answer is incorrect if more than one word entered e.g open it instead of just open so added prompt 'enter one word'
  * in bedroom 2 escape with item other than rope
## Testing
### Validation
Validation of the Python code was carried out by [PEP8](http://pep8online.com/). No errors were found.
![alt-text](assets/images/pep8.png)


### Manual Testing
The options and flow were checked manually and all passed. The tests conducted can be seen [here:](https://docs.google.com/spreadsheets/d/1NUVHJ0VQ0orWFZ3Bh9MgGXAYShW9a5Ki2Rw6T_ssCLE/edit?usp=sharing)
![alt-text](assets/images/test_sheet.png)
## Deployment
The application uses Heroku for deployement

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
The story content was developed by this author.