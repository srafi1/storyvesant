#!usr/bin/python

import os, sqlite3

def upass_get(usar):
	cmd = "SELECT password FROM users WHERE username = '%s'" % (usar)
	db_name = "upass.db"
	dab = sqlite3.connect(db_name)
	c = dab.cursor()
	Pass =	c.execute(cmd)
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
	pUser = user
	pPass = password


