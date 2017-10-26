#!usr/bin/python

import os, sys, sqlite3

def create_story(title, username):
	db_name = "data/storydb.db"
    dab = sqlite3.connect(db_name)
    c = dab.cursor()
    cmd = "SELECT "
    cmd = "INSERT INTO Stories values('%s','%s',)
    