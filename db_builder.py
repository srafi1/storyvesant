import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O
import os #Used for os.remove()

f="discobandit.db"
os.remove(f) #Used During Testing to remove file at the beginning

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops


def makeTables():
    command= "CREATE TABLE users(username TEXT, password TEXT, story_edits BLOB)"
    c.execute(command);
    command = "INSERT INTO users VALUES('a', 'a', 'a')"
    c.execute(command);

makeTables();
