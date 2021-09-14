from config import config_options
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

#initializing extensions
bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):
    #initialize the application
    app = Flask(__name__)
    #set up configurations
    app.config.from_object(config_options[config_name])
    #initializing extensions
    bootstrap.init_app(app)
    db.init_app(app)

    #Register blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

     # setting config
    from .request import configure_request
    configure_request(app)

    return app
    
#from app import views
#from app import error