# Escape from prison

## Introduction:

Escape from prison is a choose your own adventure game. It is targeted at users who would like to play an interactive story where their decisions will influence how the game story plays out.
The game was created and written using Python. It is a simple game where the player must make a choice that will allow him to complete the game successfully or will end the game with a negative result and will have to start the adventure from the beginning.

## Player's task:

On the first screen, the player will be asked to enter his name.
Thanks to this, he will be able to feel that he is part of the game. Because the name you give at the beginning will appear in subsequent stages of the adventure.
His task is to read the game script and at the right moment, he will have to make a choice by entering in the designated field one of the two prepared answers, which are in brackets at the end of the question posed to the player.
If the player makes the correct choices, he will finish the game successfully. However, if he makes a wrong choice, he will lose and will be able to try to complete the game again.

## Technologies Used: 

* **Python**: programing language
* **CodeAnywhere**: online IDE
* **GitHub**: for host repository
* **Heroku**: app launcher

## Testing:

I chose Python Syntax Checker PEP8:

![Screenshot of result of the test](/assets/img/test%20pep8.jpg)

## Deployment:

### Steps to deploy site using Heroku:

* On the Heroku dashboard, select "New" and click "Create new app"
    - Create a unique app name
    - Select your region
    - Click "Create app"
* Go to the settings tab:
    - Scroll down to the config vars section and select "Reveal Config Vars"
    - Add necessary config vars
    - In this case, in the key field enter "PORT" and the value field enter "8000"
    - Click "Add"
    - Scroll down to Buildpacks and click "Add buildpack"
    - Add the necessary buildpacks.
    - In this case, select "python" and click "Save changes"
    - Then, select "node.js" and click "Save changes"
* Go to the Deploy tab:
    - Select GitHub and confirm connection to GitHub account
    - Search for the repository and click "Connect"
    - Scroll down to the deploy options
    - Select automatic deploys if you would like automatic deployment with each new push to the GitHub repository
    - In manual deploy, select which branch to deploy and click "Deploy Branch"
    - Heroku will start building the app
* The link to the app can be found at the top of the page by clicking "Open app"

## Acknowledgements: 

I'd like to thank my mentor, Brian Macharia, for providing excellent advice and feedback during this project.