from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY']= 'sdafgsdhsk'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:root@localHost:5432/flask_db"

db = SQLAlchemy(app)

from routes import *

if __name__ == '__main__':
    app.run(debug=True)

