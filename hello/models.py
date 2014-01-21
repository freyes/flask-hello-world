from datetime import datetime
from flask.ext.sqlalchemy import SQLAlchemy
from hello.core import app


db = SQLAlchemy(app)


class TodoItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    created_at = db.Column(db.DateTime(), default=datetime.now)

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return '<TodoItem %r>' % self.title
