from flask import Flask

import os,requests

app = Flask(__name__)

@app.route('/', methods =['GET'])
def hello_world():
    return "<p>Hello, World!</p>"


 