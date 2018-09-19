from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
# Secret Key protects against modifying cookies, forgery attacks.
app.config['SECRET_KEY'] = 'some secret key'
# Configuring the dB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# An instance of a database
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

# Tells the extension(login_required) where the login route is located.
# Therefore this code redirects the user to the login page.
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from app import routes
