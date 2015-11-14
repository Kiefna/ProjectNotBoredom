import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello Earth!!!!! You globuous mass of dirt!!!'
