from app.config import DevConfig
from flask import Flask

#initialize the application
app = Flask(__name__)

#set up configurations
app.config.from_object(DevConfig)

from app import views