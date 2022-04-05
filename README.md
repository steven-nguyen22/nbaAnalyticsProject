
# NBA Data Analytics
## How to setup Django backend:
1. Download an IDE (Pycharm or Visual Studio Code)
2. Make sure python3.9 is installed. https://www.python.org/downloads/ (only if using Visual Studio Code)
3. Make sure the latest version of pip is installed. (run "python get-pip.py" in IDE terminal)
4. Command line: git clone https://github.com/ucr-cs180-fall21/cs180project-021-team-wow.git (in IDE terminal)
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

## How to create a function
1. Under the pages directory, the files views.py and urls.py will be used to create backend functions.
2. views.py : where you write your function to view for front end. Reverse engineer if needed.
3. urls.py : Under pages directory, NOT config directory, is where we initialize our function from views.py
    path('front-end-function-name', file-name.function-name, name='function-name'), ````rename front-end-function-name to frontend action name(check index.html for example). Rename function-name to the function name in views.py,  rename file-name to .py filename consisting of function. 

## If there is errors pulling from origin
1. git fetch --all
2. git reset --hard origin/{{your branch name}}
