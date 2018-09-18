from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
# Secret Key protects against modifying cookies, forgery attacks.
app.config['SECRET_KEY'] = 'some secret key'
# Configuring the dB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# An instance of a database
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from app import routes