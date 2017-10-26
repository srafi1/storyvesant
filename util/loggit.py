#!usr/bin/python

import os, sys, sqlite3


def upass_get(usar):
    db_name = "upass.db"
    dab = sqlite3.connect(db_name)
    c = dab.cursor()
    cmd = "SELECT password FROM users WHERE username = '%s'" % (usar)
    Pass =    c.execute(cmd)
    nPass = ""
    for row in Pass:
        nPass = str(row[0])
    return nPass

def auth(usar,passwad):
    pUser = usar
    pPass = hash(passwad)
    '''
    stat_code -1 = nothing in user input
    stat_code 0 = bad user or password
    stat_code 1 = good
    '''
    upassget = upass_get(usar)
    if (upass_get(usar) == ""):
        return -1
    elif (pPass == int(upassget)):
        return 1
    else:
        return 0

def register(user, password):
    db_name = "upass.db"
    dab = sqlite3.connect(db_name)
    c = dab.cursor()
    pPass = password
    cmd = "SELECT * FROM users WHERE username = '%s'" % (user)
    check = c.execute(cmd)
    nPass = ''
    for row in check:
        nPass = str(row[0])
    if nPass != "":
        print "User "+user+" already exists"
        return 0
    print "User will be added."
    cmd = "INSERT INTO users VALUES ('%s', '%s')" % (user, str(hash(pPass)))
    c.execute(cmd)
    print user+" added."
    dab.commit()
    return 1

def check_for_user(user):
    db_name = "upass.db"
    dab = sqlite3.connect(db_name)
    c = dab.cursor()
    cmd = "SELECT * FROM users WHERE username = '%s'" % user
    c.execute(cmd)
    return len(c.fetchall()) != 0
