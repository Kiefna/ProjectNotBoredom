import os
from flask import Flask, render_template

app = Flask(__name__)

#if we make the url have a <param>
@app.route('/<message>')
def message(message): # we pass it into the controller
    return render_template("index.html", message=message) # and we can use it in the view

@app.route('/')
def index():
    return render_template("index.html", message="hello world")
