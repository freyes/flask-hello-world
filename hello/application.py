# all the imports
import sqlite3
import hashlib
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

@application.route("/sha1/<foo>/<n>")
def calculate_sha1(foo, n):
    output = foo
    for i in range(max(1, int(n))):
        output = hashlib.sha1(output).hexdigest()

    return output


if __name__ == "__main__":
    application.run(host='0.0.0.0', debug=True)
