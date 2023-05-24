from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os


app = Flask(__name__, static_url_path = '/static')


app.config['SECRET_KEY'] = '4c96d977af696b80a620fb703c211c32'
if os.gentv("DATABASE_URL"):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.gentv("DATABASE_URL")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'


database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_menager = LoginManager(app)
login_menager.login_view= 'login_criarconta'
login_menager.login_message_category = 'alert-info'


from comunidadeimpressionadora import routes
