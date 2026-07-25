# NOTE: To run the app in the integrated terminal run:
#       "flask run" OR
#       "python -m flask run"
#       which starts the Flask development server.

# support for regular expressions
import re

# specific date/time and related types
from datetime import datetime

# import Flask
from flask import Flask, render_template

from . import app


# the app.route decorator maps the "/" URL route --> to this function.
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/contact/")
def contact():
    return render_template("contact.html")


@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name=None):
    return render_template("hello_there.html", name=name, date=datetime.now())


@app.route("/api/data/")
def get_data():
    return app.send_static_file("data/data.json")
