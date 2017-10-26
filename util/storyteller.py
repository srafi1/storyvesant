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