# After the Party
After the Party Live Link [here](https://after-the-party.herokuapp.com/)
## Overview
[Afer the Party Flowchart](https://github.com/siobhanlgorman/After-the-Party/blob/main/documentation/After%20the%20party.png)
After the Party is a lighthearted zombie escape game. The player wakes up after a party in an unfamiliar house where everyone else seems to have turned into zombies.
## Features
## Screenshots
## Flowchart
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
## Deployment
The application uses Heroku for deployement

### To create the application:
* first create the requirements file the Heroku will use to import the dependencies required for deployment: type `pip3 freeze > requirements.txt`
* navigate to the [Heroku](https://www.heroku.com/) website
* create an account by entering your email address and a password
* activate the account through the authentication email sent to your email account
* click the new button and select create a new app from the dropdown menu
* enter a name for the application which must be unique, in this case the app name is after-the-party
* select a region, in this case Europe
* click create app

### Heroku settings
* From the horizontal menu bar select 'Settings'
* In the config vars section where sensitive data is stored e.g. creds.json (in gitignore file) in the field for key enter CREDS from Gitpod workspace copy entire creds.json file into value field then click 'add' (This step is included but it was not necessary to set any config vars for this project)
* In the buildpacks section where further necessary dependencies are installed click 'add buildpack'. Select 'Python' first and click 'save changes'. Next click 'node.js' and then click 'save changes' again. The 'Python' buildpack must be above the 'node.js' buildpack'. The can be clicked on and dragged to change the order if necessary
### Deployment
* In the top menu bar select 'Deploy'
* In the deployment methos section select 'Github' and click the connect to Github button to confirm
* In the 'search' box enter the Github repository name for the project. Click search and then click connect to link the heroku app with the Github repository. The box will confirm connected to in this case [After the Party](https://github.com/siobhanlgorman/After-the-Party)
* Scroll down to select either automatic or manual deployment. For this project automatic deployment was selected. If you wish to select automatic deployment select the button 'Enable Automatic Deploys'. This will rebuild the app every time a change is pushed to Github. If you wish to manually deploy click the button 'Deploy Branch'. The default 'Master' option in the dropdown menu should be selected in both cases
* 


### Live Deployment
### Local Deployment
## Credits
### Code
  [Learn Python by making a text-based adventure game](https://coding-grace-guide.readthedocs.io/en/latest/guide/lessonplans/beginners-python-text-based-adventure.html)
## Content