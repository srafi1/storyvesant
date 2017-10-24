#!usr/bin/python
from flask import Flask, session, render_template, request, redirect, url_for, flash
import os, sqlite3

app = Flask(__name__)
app.secret_key = os.urandom(32)

def auth(user,passo,upass):
	'''
	stat_code -1 = bad username
	stat_code 0 = bad password
	stat_code 1 = good
	'''
	stat_code = -1
	if user in upass:
		stat_code+=1
		if passo == upass[user]:
			stat_code+=1
	return stat_code


def auth(usar,passwad):
	db_name = "upass.db"
	cmd = ""
	if "user" in request.args and "passo" in request.args:
		username = request.args["user"]
		password = hash(request.args["passo"])


def register(usar, passwad):

@app.route("/")
def landing():
	return render_template("index.html", title = "welcome")
@app.route("/login")
def login():
	print("hello")
if __name__ == "__main__":
    app.debug = True
    app.run()