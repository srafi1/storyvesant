import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O
import os #Used for os.remove()

f="storyvesant.db"
os.remove(f) #Used During Testing to remove file at the beginning


def makeTables():
    db = sqlite3.connect(f) #open if f exists, otherwise create
    c = db.cursor()    #facilitate db ops

    command= "CREATE TABLE users(username TEXT, password TEXT, user_id INTEGER, story_edits TEXT)"
    c.execute(command)
    
    #Individual stories should have an ID number
    #Users should be referred to by their ID numbers
    command= "CREATE TABLE stories(title TEXT, creator_id INTEGER, story_id INTEGER)"
    c.execute(command)
    
    ##command = "INSERT INTO users VALUES('a', 'a', 'a')"
    ##c.execute(command);
    db.commit() #save changes
    db.close()  #close database

def new_story(title,uID):
    db = sqlite3.connect(f) #open if f exists, otherwise create
    c = db.cursor()    #facilitate db ops

    command="INSERT INTO stories("+title+","+uID+","+\ #find last number add one
      "1)"
    c.execute(command)
        
    db.commit() #save changes
    db.close()  #close database        
    
def new_story_table(title):#Makes new table for a new story
    db = sqlite3.connect(f) #open if f exists, otherwise create
    c = db.cursor()    #facilitate db ops
    
    command= "CREATE TABLE "+title+"(edit TEXT, edit_id INTEGER, user_id INTEGER)"
    c.execute(command)

    db.commit() #save changes
    db.close()  #close database


def newUser(uname, pword):
    db = sqlite3.connect(f) #open if f exists, otherwise create
    c = db.cursor()    #facilitate db ops    

    command = "SELECT COUNT(*) FROM users"
    count = c.execute(command)[0][0]
    command = "INSERT INTO users VALUES(uname, pword," + str(count) + ",'NULL')"
    c.execute(command)

    db.commit() #save changes
    db.close()  #close database

    
makeTables();

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

newUser("ibnul", "jahan")
newUser("name", "pass")

