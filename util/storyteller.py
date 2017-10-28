#!usr/bin/python

import os, sys, sqlite3, datetime

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
    cmd = "CREATE TABLE %s(added_text TEXT, username TEXT, edit_month INT, edit_day INT, edit_ID INT)" %(title)
    c.execute(cmd)
    dab.commit()
    dab.close()
    return 1

#return list of dictionaries with .title and .last-sentences.
def get_story_list():
    cmd = "SELECT * FROM Stories ORDER BY id DESC"
    db_name = "data/upass.db"
    dab = sqlite3.connect(db_name)
    c = dab.cursor()
    stories = c.execute(cmd)
    storyarr = []
    storydict = {}
    for story in stories:
        storydict["title"] = str(story[0])
        storydict["last_sentence"] = get_last_sentence(story[0])
        storyarr.append(storydict.copy())
    return storyarr

#returns last sentence in a story
def get_last_sentence(story):
    cmd = "SELECT added_text FROM %s ORDER BY edit_id DESC"%(story)
    db_name = "data/upass.db"
    dab = sqlite3.connect(db_name)
    c = dab.cursor()
    c.execute(cmd)
    sentence = c.fetchone()
    return str(sentence[0])
