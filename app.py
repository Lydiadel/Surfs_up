# 1. import flask
from flask import Flask

# Create a new flask instance
app = Flask(__name__)

# Create a flask route
@app.route('/')
def helloWorld():
    return 'Hello World'
