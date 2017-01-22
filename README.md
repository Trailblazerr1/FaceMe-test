# FaceMe: A visual of your fb profile
![](https://github.com/Trailblazerr1/FaceMe/blob/master/faceme/www.GIFCreator.me_kYNyES.gif)  

## What it does
Shows you some interesting visualizations of your facebook account.


## Producing locally  
Getting a working local copy of website requires a few steps: getting a copy of the site's code, and then adding lots of dependencies.  
  
You’ll need to have Python 3.5 available for code to work. Python 3.5.1 is installed on Ubuntu 16.04 by default. You can verify that by running the command _python3 --version_ in a terminal.

1.  Setup a _project_ folder to store everything:  
	```
    $ mkdir project     
      
    $ cd project
    ```
2.  Get a copy of the site's code by running a _git clone_:         

	```
    $ git clone https://github.com/Trailblazerr1/FaceMe-test.git      
    ```
3.  Now install all the dependencies:  

	```
    $ cd FaceMe-test
    $ pip3 install -r requirements.txt
```
	If it throws error try installing pip by:
    ```
    $ sudo apt-get install python3-pip
```
4. Lastly sync the models by:

	``` 
	$ cd faceme
    $ python3 manage.py makemigrations
    $ python3 manage.py migrate
    $ python3 manage.py runserver
 ```
5. Now the terminal should end up looking like this:

	```
	Performing system checks...
	System check identified no issues (0 silenced).
    Django version 1.10.1, using settings 'faceme.settings'
	Starting development server at http://127.0.0.1:8000/
	Quit the server with CONTROL-C.
```
6. Now skim over to     

	[127.0.0.1:8000/data/graph](127.0.0.1:8000/data/graph/)
    
	in your favourite browser.  
    
You now have a working  environment!

## For contribution 
   See [issues](https://github.com/Trailblazerr1/FaceMe-test/issues)

The data provided here is mock-data and it doesn't communicates with fb in realtime.For further info see [this](https://github.com/Trailblazerr1/FaceMe).   
     
Made with love by: Django, d3.js, postgreSQL,fb graph api
