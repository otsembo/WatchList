from app.config import DevConfig
from flask import Flask
from flask_bootstrap import Bootstrap

#initialize the application
app = Flask(__name__, instance_relative_config=True)

#set up configurations
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

#initializing extensions
bootstrap = Bootstrap(app)

from app import views
from app import error