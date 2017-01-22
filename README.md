# FaceMe: A visual of your fb profile
![](https://github.com/Trailblazerr1/FaceMe/blob/master/faceme/www.GIFCreator.me_kYNyES.gif)  

## What it does
Shows you some interesting visualizations of your facebook account.

## For contribution 


## Producing locally  
Getting a working local copy of website requires a few steps: getting a copy of the site's code, and then adding lots of dependencies.  
  
You’ll need to have Python 3.5 available for code to work. Python 3.5.1 is installed on Ubuntu 16.04 by default. You can verify that by running the command _python3 --version_ in a terminal.

1.  Setup a _FaceMe_ folder to store everything:  

- Clone the repo by _git clone https://github.com/Trailblazerr1/FaceMe-test.git_.  
- pip3 install -r requirements.txt.  
- Change to directory which has manage.py.
- _python3 manage.py makemigrations_ (This might throw an error, keep going).  
- _python3 manage.py migrate_ (This might throw an error, keep going).  
- _python3 manage.py runserver_.
- Go to [127.0.0.1:8000/data/graph](127.0.0.1:8000/data/graph) 

The data provided here is mock-data and it doesn't communicates with fb in realtime.For further info see [this](https://github.com/Trailblazerr1/FaceMe).   
     
Made with love by: Django, d3.js, postgreSQL,fb graph api
