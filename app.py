#!usr/bin/python

from flask import Flask, session, render_template, request, redirect, url_for, flash
from functools import wraps
import os, sys, sqlite3
import util.loggit as loggit
import util.storyteller as bard
import util.db_builder as db

app = Flask(__name__)
app.secret_key = os.urandom(32)

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if "user" in session:
            return func(*args, **kwargs)
        flash("You need to login first")
        return redirect("/login")
    return wrapper

@app.route("/")
def landing():
    return render_template("index.html")

@app.route("/login", methods = ["GET", "POST"])
def login_route():
    if request.method == "POST":
        uname = request.form.get("uname") 
        pword = request.form.get("pword") 
        auth_result = loggit.auth(uname, pword)
        if auth_result == 1:
            session['user'] = uname
            return redirect("/")
        elif uname == "" or pword == "":
            flash("Enter both username and password")
        else:
            flash("Bad username or password")
    return render_template("login.html")

@app.route("/logout")
def logout_route():
    if "user" in session:
        session.pop("user")
    return redirect("/")
        
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
        if loggit.check_for_user(uname):
            flash("That username is taken")
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
    return render_template("register.html")

@app.route("/create", methods = ["GET", "POST"])
@login_required
def create_story():
    if request.method == "POST":
        title = request.form.get("title")
        body = request.form.get("body")
        valid = True
        if title == "":
            flash("Please enter a title")
            valid = False
        if body == "":
            flash("Please enter a body")
            valid = False
        if bard.check_story_exists(title):
            flash("That story already exists")
            valid = False
        if valid:
            bard.create_story(title,session["user"])
            bard.add_to_story(title,session["user"],body)
            return redirect("/")
    return render_template("create_story.html")

@app.route("/stories")
@login_required
def list_stories_route():
    storylist = bard.get_story_list()
    return render_template("list_stories.html",stories = storylist)

@app.route("/profile", methods = ["GET", "POST"])
@login_required
def profile_route():
    if request.method == "POST":
        old_pword = request.form.get("old_pword") 
        pword = request.form.get("pword") 
        pword2 = request.form.get("pword2") 
        valid = True
        if old_pword == None or old_pword == "":
            flash("Enter your current password")
            valid = False
        if pword == None or pword == "":
            flash("Enter a new password")
            valid = False
        if pword != pword2:
            flash("Passwords do not match")
            valid = False
        if valid:
            if loggit.change_pass(session["user"], old_pword, pword):
                return redirect("/")
            flash("Incorrect current password")
    return render_template("profile.html")

@app.route("/view/<int:story_id>")
@login_required
def view_story(story_id):
    title = bard.get_story_title(story_id)    
    if title:
        story = {"title":title, 
                "last_sentence":bard.get_last_sentence(title),
                "body":bard.get_full_story(title).replace("\n", "<br/>"),
                "id":story_id
                }
        if bard.user_edited_story(title, session["user"]):
            return render_template("view_full_story.html", story = story)
    else:
        story = None
    return render_template("view_story.html", story = story)

@app.route("/edit/<int:story_id>", methods = ["GET", "POST"])
@login_required
def edit_story(story_id):
    title = bard.get_story_title(story_id)
    if request.method == "POST":
        valid = True
        next_sentence = request.form.get("next_sentence")
        if next_sentence == None or next_sentence == "":
            flash("Please enter the next sentence")
            valid = False
        if valid:
            bard.add_to_story(title, session["user"], next_sentence)
            return redirect("/view/%d"%story_id)
    if title:
        story = {"title":title, 
                "last_sentence":bard.get_last_sentence(title),
                "id":story_id
                }
        if bard.user_edited_story(title, session["user"]):
            return redirect("/view/%d"%story_id)
    else:
        story = None
    return render_template("edit_story.html", story = story)

if __name__ == "__main__":
    if not os.path.exists("data/storyvesant.db"):
        db.make_tables()
    app.debug = True
    app.run()
