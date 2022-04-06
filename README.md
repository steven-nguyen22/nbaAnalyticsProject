
# NBA Dataset Analytics
## Project Description
- This project was interesting to our group because we are all sports fans and wanted to work with a dataset that reflected an interest that the group shared. The main goal of this project was to allow users to search, enter, delete, update, backup, and perform interesting analytics on the given dataset. For this project we used HTML/CSS for the front-end and Python/Django for the back-end. Our analytics include displaying the top 5 team wins for a given season, displaying the 3 pts made for a given player, the average points scored between the home team vs the away team, displaying the top scorers of a given team for a season, and comparing the fg % for two different players. 
- Dataset: https://www.kaggle.com/datasets/nathanlauga/nba-games

## Team
[Carlos Loeza](https://github.com/CarlosLoeza)

[Jeff Nguyen](https://github.com/JeefKeef)

[Brian Yang](https://github.com/brianyang9)

[Gina Metzidaki](https://github.com/ginametzidaki)

[Steven Nguyen](https://github.com/steven-nguyen22)

## How to setup Django backend
1. Download an IDE (Pycharm or Visual Studio Code)
2. Make sure python3.9 is installed. https://www.python.org/downloads/ (only if using Visual Studio Code)
3. Make sure the latest version of pip is installed. (run "python get-pip.py" in IDE terminal)
4. Command line: git clone https://github.com/steven-nguyen22/nbaAnalyticsProject.git (in IDE terminal)
5. Command line: pip install -r requirements.txt (in IDE terminal)

## How to run server
1. Command line: python3 config/manage.py runserver (in IDE terminal)
2. Open web browser, enter url: http://127.0.0.1:8000/
3. If you encounter the following problem: 
![problem](https://github.com/ucr-cs180-fall21/cs180project-021-team-wow/blob/main/potential%20error%20message.png)
    - Open csvreadwrite.py in config -> pages -> src -> csvreadwrite.py
    - Remove the "../" (highlighted in the image) in lines 22, 51, 91, 105, and 128
 
## High-level Overview 
1. backup folder - contains updated csv files when new data is inputted and backed up
2. data folder - contains original csv files from the NBA dataset (https://www.kaggle.com/nathanlauga/nba-games) 
3. config/pages/templates folder - contains all of our html files 
4. config/pages/static folder - contains all of our css and images used in the webpage 
5. config/pages/urls.py - contains all of our paths to navigate around the webpage
6. config/pages/views.py - code that calls our backend functions for our analytics/features
7. config/pages/src/utils.py - code for our backend functions
8. config/pages/src/csvreadwrite.py - code that read/writes to our csv files

## Screenshots
Home Page
![Home Page](https://github.com/steven-nguyen22/nbaAnalyticsProject/blob/main/images/homepage.png)
Search Player Page
![Search Player Page](https://github.com/steven-nguyen22/nbaAnalyticsProject/blob/main/images/searchPlayer.png)
Update Team Wins Page
![Update Team Wins Page](https://github.com/steven-nguyen22/nbaAnalyticsProject/blob/main/images/updateTeamWins.png)
Top 5 Team Wins Table
![Top 5 Team Wins Page](https://github.com/steven-nguyen22/nbaAnalyticsProject/blob/main/images/top5TeamWins.png)
Compare Two Players
![Compare Two Players](https://github.com/steven-nguyen22/nbaAnalyticsProject/blob/main/images/compare2Players.png)
