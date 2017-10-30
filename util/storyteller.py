#!usr/bin/python

import os, sys, sqlite3, datetime

def create_story(title, username):
    cmd = "SELECT id FROM Stories ORDER BY id DESC"
    db_name = "data/storyvesant.db"
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
    cmd = "CREATE TABLE '%s'(added_text TEXT, username TEXT, edit_month INT, edit_day INT, edit_ID INT)" %(title)
    c.execute(cmd)
    dab.commit()
    dab.close()
    return 1

def add_to_story(title,username,addedtext):
    cmd = "SELECT edit_id FROM '%s' ORDER BY edit_id DESC"%(title)
    db_name = "data/storyvesant.db"
    dab = sqlite3.connect(db_name)
    c = dab.cursor()
    c.execute(cmd)
    nums = c.fetchone()
    if (nums == None):
        #print "0"
        nums = 0
    else:
        nums = nums[0]
    d = datetime.date.today()
    mon = d.month
    day = d.day
    cmd = "INSERT INTO '%s' values('%s','%s',%i,%i,%i)"%(title,addedtext,username,mon,day,1+nums)
    c.execute(cmd)
    dab.commit()
    dab.close()
    return 1    

def get_story_title(story_id):
    cmd = "SELECT * FROM Stories WHERE id = %i"%(story_id)
    db_name = "data/storyvesant.db"
    dab = sqlite3.connect(db_name)
    c = dab.cursor()
    story = c.execute(cmd)
    storytitle = story.fetchone()
    if storytitle == None:
        return None
    return str(storytitle[0])

#return list of dictionaries with .title and .last-sentences.
def get_story_list():
    cmd = "SELECT * FROM Stories ORDER BY id DESC"
    db_name = "data/storyvesant.db"
    dab = sqlite3.connect(db_name)
    c = dab.cursor()
    stories = c.execute(cmd)
    storyarr = []
    storydict = {}
    for story in stories:
        storydict["title"] = str(story[0])
        storydict["id"] = int(story[2])
        storydict["last_sentence"] = get_last_sentence(story[0])
        storyarr.append(storydict.copy())
    return storyarr

def check_story_exists(title):
    cmd = "SELECT * FROM Stories WHERE title = '%s'" % title
    db_name = "data/storyvesant.db"
    dab = sqlite3.connect(db_name)
    c = dab.cursor()
    c.execute(cmd)
    story = c.fetchone()
    if story == None:
        return False
    return True

def get_full_story(title):
    cmd = "SELECT added_text FROM '%s' ORDER BY edit_id ASC"%(title)
    db_name = "data/storyvesant.db"
    dab = sqlite3.connect(db_name)
    c = dab.cursor()
    allwords = c.execute(cmd)
    finalsay = ""
    for sentence in allwords:
        finalsay+=str(sentence[0])+"\n"
    return finalsay

def user_edited_story(title, user):
    cmd = "SELECT * FROM '%s' WHERE username = '%s'" % (title, user)
    db_name = "data/storyvesant.db"
    dab = sqlite3.connect(db_name)
    c = dab.cursor()
    c.execute(cmd)
    if c.fetchone():
        return True
    return False

#returns last sentence in a story
def get_last_sentence(story):
    cmd = "SELECT added_text FROM '%s' ORDER BY edit_id DESC"%(story)
    db_name = "data/storyvesant.db"
    dab = sqlite3.connect(db_name)
    c = dab.cursor()
    c.execute(cmd)
    sentence = c.fetchone()
    if sentence == None:
        return ""
    return str(sentence[0])
