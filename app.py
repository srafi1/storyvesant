#!usr/bin/python
from flask import Flask, session, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)


@app.route("/")
def landing():
	return render_template("index.html", title = "welcome")
@app.route("/login")
def login():
	print("hello")
if __name__ == "__main__":
    app.debug = True
    app.run()