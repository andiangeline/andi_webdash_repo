#web dashboard programming module 6

#in atom
#packages-platformio ide terminal-new terminal
#don't need to enter virtual env at this point
#okteto login
#okteto namespace #syncs with kubernetes credentials on our laptop
#okteto up

#for pc, once connected with okteto, use the mac command to access "webdash2"
#source webdash2/bin/activate

#then we need to do a bunch of pip install
#python -m pip install --upgrade pip

#pip install fastapi-sqlalchemy
#sqlalchemy popular OOP mapper to database
#it extracts the sql statement in database
#in terms of architecture, it's more fluid to use sqlalchemy

#pip install async-exit-stack
#pip install async-generator
#these are used by fastapi as well
#asynchronise, better at managing requests
#django is synchonise
#node.js is javascript framework
#fastapi is python

#pip install psycopg2-binary

#pip install -r requirements.txt
#also install the files from your requirements.txt file
#because this is a development environment that goes to sleep
#we need to re-install those libraries everytime we re-connect with our testing environment after some period of time

#create 3 python files in our app folder
#database.py #in this file we write the command to connect to our database
#models.py  #in this file we write classes that represent our database tables
#crud.py  #in this file we write functions that query our database tables

#python -m pip freeze > requirements.txt
