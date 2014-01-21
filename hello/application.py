# all the imports
import sqlite3
import hashlib
from pyinfo import pyinfo
from flask import Flask, render_template, request, redirect
from hello.core import app
from hello.models import TodoItem, db


@app.route("/")
def index():
    return "hello world"


@app.route("/pyinfo")
def info():
    return pyinfo()

@app.route("/sha1/<foo>/<n>")
def calculate_sha1(foo, n):
    output = foo
    for i in range(max(1, int(n))):
        output = hashlib.sha1(output).hexdigest()

    return output

@app.route("/todo")
def list_todo():
    return render_template("list_todo.djhtml", todos=TodoItem.query.all())


@app.route("/todo/new", methods=["GET", "POST"])
def new_todo():
    if request.method == "GET":
        return render_template("new_todo.djhtml")

    t = TodoItem(request.form["todo_title"])
    db.session.add(t)
    db.session.commit()
    return redirect("/todo", 302)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
