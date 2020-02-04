import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)

from blog.core.views import core
from blog.error_handler.handlers import errors
from blog.users.views import users

app.register_blueprint(core)
app.register_blueprint(errors)
app.register_blueprint(users)
###############################################
##############Database Setup###################
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite') 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)
###############################################
############Login Configuration################
login_manager = LoginManager()

login_manager.init_app(app)
login_manager.login_view = 'users.login'
###############################################
