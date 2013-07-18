# all the imports
import sqlite3
from pyinfo import pyinfo
from flask import Flask


# create our little application :)
app = Flask(__name__)
app.config["DEBUG"] = True
app.config["SECRET_KEY"] = 'development key'


@app.route("/")
def index():
    return "hello world"


@app.route("/pyinfo")
def info():
    return pyinfo()


if __name__ == "__main__":
    app.run()
