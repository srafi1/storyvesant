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

def auth(usar,passwad):
	db_name = "upass.db"
	cmd = ""
	pUser = usar
	pPass = hash(passwad)
	'''
	stat_code -1 = bad username
	stat_code 0 = bad password
	stat_code 1 = good
	'''
	stat_code = -1
	stat_code = -1
	if user in upass:
		stat_code+=1
		if passo == upass[user]:
			stat_code+=1
	return stat_code

@app.route("/")
def landing():
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
