# After the Party
After the Party Live Link [here](https://after-the-party.herokuapp.com/)
## Overview
[Afer the Party Flowchart](https://github.com/siobhanlgorman/After-the-Party/blob/main/documentation/After%20the%20party.png)
After the Party is a lighthearted zombie escape game. The player wakes up after a party in an unfamiliar house where everyone else seems to have turned into zombies.
## Features
### Existing Features
### Run Program button
### Terminal Area
Screenshots here
### Program Structure
The flowchart created during the planning stage can be viewed [here](https://github.com/siobhanlgorman/After-the-Party/blob/main/assets/after_the_party.png)

## Technologies
### Languages.. 
  * Python
### Other Technologies and Libraries
* Github
* Git
* Heroku
## Known Issues/Bugs

  * in landing function user answer is incorrect if more than one word entered e.g open it instead of just open so added prompt 'enter one word'
  * in bedroom 2 escape with item other than rope
## Testing
### [PEP8](http://pep8online.com/)
### Manual Testing
The options and flow were checked manually and all passed. The tests conducted can be seen [here:](https://docs.google.com/spreadsheets/d/1NUVHJ0VQ0orWFZ3Bh9MgGXAYShW9a5Ki2Rw6T_ssCLE/edit?usp=sharing)

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
2. Go to the 'Config Vars' section (where sensitive data is stored e.g. the data from the creds.json file in Github gitignore file).  In the field for 'key' enter CREDS from Gitpod workspace copy entire creds.json file into 'value' field then click 'add' (This step is included but it was not necessary to set any config vars for this project).
3. In the buildpacks section, where further necessary dependencies are installed, click 'add buildpack'. Select 'Python' first and click 'save changes'. Next click 'node.js' and then click 'save changes' again. The 'Python' buildpack must be above the 'node.js' buildpack'. They can be clicked on and dragged to change the order if necessary.
### Deployment
1. In the top menu bar select 'Deploy'.
2. In the 'Deployment method' section select 'Github' and click the connect to Github button to confirm.
3. In the 'search' box enter the Github repository name for the project. Click search and then click connect to link the heroku app with the Github repository. The box will confirm that heroku is connected to the repository which in this case is [After the Party](https://github.com/siobhanlgorman/After-the-Party).
4. Scroll down to select either automatic or manual deployment. For this project automatic deployment was selected. If you wish to select automatic deployment select the button 'Enable Automatic Deploys'. This will rebuild the app every time a change is pushed to Github. If you wish to manually deploy click the button 'Deploy Branch'. The default 'Master' option in the dropdown menu should be selected in both cases.
5. When the app is deployed a message 'Your app was successfully deployed' will be shown. Click 'view' to see the deployed app in the browser. The live deployment of the project can be seen [here](https://after-the-party.herokuapp.com/)
6. The app starts automatically and can be restarted by pressing the 'Run Program' button.
### Forking the Repository
If you wish to fork the repository to make changes without affecting the original you can fork the repository
1. Navigate to the [After the Party repository](https://github.com/siobhanlgorman/After-the-Party).
2. Click the 'Fork' button at the top right of the page.
3. A forked copy of the repository will appear in your Repositories page.
### Cloning the Repository
1. On [GitHub](https://github.com/) navigate to the main page of the repository.
2. Above the list of files click the dropdown code menu.
3. Select the https option and copy the link.
4. Open the GitPod Bash terminal.
5. Change the current working directory to the desired destination location.
6. Type the git clone command with the copied URL: `git clone https://github.com/siobhanlgorman/After-the-Party.git`.
7. Press enter to create the local clone.


## Credits
### Code
  [Learn Python by making a text-based adventure game](https://coding-grace-guide.readthedocs.io/en/latest/guide/lessonplans/beginners-python-text-based-adventure.html)
## Content