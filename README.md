# Run Application

This repo is created for the assignment 4 of our course Introduction to Software Systems.

## To run it locally
- Run `git clone https://gitlab.com/jalees.jahanzaib/2018101001intosoftwaresys/tree/master/Assignments/Assignment-4/` to clone this repository.
- Run `virtualenv env` to create a virtual environment for the project.
- Run `pip3 install -r requirements.txt` to install all the dependencies.
- Run `flask run` to run the app in your localhost.
- Visit `127.0.0.1:5000` for the website.

## API reference
- `/api/generate`
    - Arguments:
        - `sz`(Required): Size of the key
        - `e`(Optional): Set the e value, defaults to `0x1001`
    - Returns `n`, `e`, `p`, `q`, `d % (p-1)`, `d % (q-1)`, `coeff`, `d`  
- `/api/encrypt`
    - Arguments(All required):
        - `message`: The message to be encrypted
        -  `n`: The public key
        -  `e`: The exponent in the public key
                 - Returns the encrypted message
                 - 
                 - 
                 - 
## Design patterns identified
- Factory pattern while initializing the database. An empty constructor is used to create an instant of the database object in the `models.py` file but the app context is added in `app.py`
- Singleton pattern while initializing the database. There cannot exist two different instants of the database object at some point of time, that is why a singleton pattern is alays used when initializing a database connection object

## Continuous integration
- Implemented continuous integration using TravisCI. The `.travis.yml` file is the config file used.
- Unit test cases written in `tests.py`
- 
## Folder Structure






1. run.py 				            #import app,db from exp7 and run app
2. exp7
    -1. __init__.py 	 	            #import flask , contain app, db, all routes
    -2. experiment.py 	            #contain database classes
    -3. templates			        #contain all html files
        index.html 			        #contain layout part of website
         other files contain the main block containing part as indicated by their name.
    4. static
        1.images                      
        2.css
            style.css               #contain css part of all html files
            some downloaded css files
        3.js
            custom.js               #contain js part of all html files
            some downloaded js files
```
