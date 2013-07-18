# all the imports
import sqlite3
from pyinfo import pyinfo
from flask import Flask


# create our little application :)
application = Flask(__name__)
application.config["DEBUG"] = True
application.config["SECRET_KEY"] = 'development key'


@application.route("/")
def index():
    return "hello world"


@application.route("/pyinfo")
def info():
    return pyinfo()


if __name__ == "__main__":
    application.run(host='0.0.0.0', debug=True)
