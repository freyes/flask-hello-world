import os
from flask import Flask


app = Flask("hello")
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_URI") or 'sqlite://'
app.config["DEBUG"] = True
app.config["SECRET_KEY"] = 'development key'
