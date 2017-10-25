#!usr/bin/python
from flask import Flask, session, render_template, request, redirect, url_for, flash
import os, sqlite3
import util.loggit as loggit

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route("/")
def landing():
    #print "login status code test: "+str(loggit.auth("admin","password"));
    #loggit.register("a","admin2")
    return render_template("index.html", title = "Welcome")

@app.route("/login")
def login_route():
    return render_template("login.html", title = "Login")

@app.route("/register", methods = ["GET", "POST"])
def register_route():
    if request.method == "POST":
        uname = request.form.get("uname") 
        pword = request.form.get("pword") 
        pword2 = request.form.get("pword2") 
        valid = True
        if uname == None or uname == "":
            flash("Enter a username")
            valid = False
        if pword == None or pword == "":
            flash("Enter a password")
            valid = False
        if pword != pword2:
            flash("Passwords do not match")
            valid = False
        if valid:
            loggit.register(uname, pword)
            return redirect("/login")
    return render_template("register.html", title = "Register")

#@app.route("/read/<int:id>")
#def read():
    

#@app.route("/edit")


if __name__ == "__main__":
    app.debug = True
    app.run()
