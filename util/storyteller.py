#!usr/bin/python

import os, sys, sqlite3

def create_story(title, username):
    cmd = "SELECT id FROM Stories ORDER BY id DESC"
    db_name = "data/upass.db"
    dab = sqlite3.connect(db_name)
    c = dab.cursor()
    c.execute(cmd)
    nums = c.fetchone()
    if (nums == None):
        print "0"
        nums = 0
    else:
        nums = nums[0]
    cmd = "INSERT INTO Stories values('%s','%s','%i')"%(title, username, nums+1)
    c.execute(cmd)
    dab.commit()
    dab.close()
    return 1

#return list of dictionaries with .title and .last-sentences.
def get_story_list():
    cmd = "SELECT * FROM Stories ORDER BY id ASC"
    db_name = "data/upass.db"
    dab = sqlite3.connect(db_name)
    c = dab.cursor()
    stories = c.execute(cmd)
    storydict = {}
    for story in stories:
        storydict["title"] = str(story[0])
        storydict["last_sentence"] = 
    print storydict
def get_last_sentence():
    cmd = "SELECT * FROM Stories ORDER BY id ASC"
    db_name = "data/upass.db"
    dab = sqlite3.connect(db_name)
    c = dab.cursor()
    stories = c.execute(cmd)