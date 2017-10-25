#!usr/bin/python
from flask import Flask, session, render_template, request, redirect, url_for, flash
import os, sqlite3

app = Flask(__name__)
app.secret_key = os.urandom(32)

def init_parse_tables():
	db_name = "upass.db"
	dab = sqlite3.connect(db_name)
	c = dab.cursor()
	cmd = ""

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

@app.route("/")
def landing():
	print auth("a","a");
	return render_template("index.html", title = "Welcome")

@app.route("/login")
def login_route():
    return render_template("login.html", title = "Login")

@app.route("/register")
def register_route():
    return render_template("register.html", title = "Register")

if __name__ == "__main__":
    app.debug = True
    app.run()
