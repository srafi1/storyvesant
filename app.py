#!usr/bin/python
from flask import Flask, session, render_template, request, redirect, url_for, flash
import os, sqlite3
import util.loggit as loggit

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route("/")
def landing():
	print "login status code test: " loggit.auth("a","a");
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
