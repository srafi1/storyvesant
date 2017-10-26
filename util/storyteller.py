#!usr/bin/python

import os, sys, sqlite3

def create_story(title, username):
	db_name = "data/upass.db"
	dab = sqlite3.connect(db_name)
	c = dab.cursor()
	cmd = "INSERT INTO Stories values('%s','%s',)"
