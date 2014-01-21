from flask import Flask


app = Flask("hello")
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_URI") or 'sqlite://'
