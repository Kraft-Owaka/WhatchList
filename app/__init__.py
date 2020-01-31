from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap


bootstrap = Bootstrap()



def create_app(config_name):
    app = Flask(__name__)
    # Create the app configurations 
    app.config.from_object(config_options[config_name])

    # Initializing flask exrensions
    bootstrap.init_app(app)
    
    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # setting config
    from .request import configure_request
    configure_request(app)

    

    

    # Will add the views and forms

    return app



    # from flask import Flask
# from flask_bootstrap import Bootstrap
# from .config import DevConfig
# from config import config_options


# # Initializing application
# app = Flask(__name__,instance_relative_config = True)

# #Setting up configuration
# app.config.from_object(DevConfig)
# app.config.from_pyfile('config.py')

# # Initializing Flask Extensions
# bootstrap = Bootstrap(app)

# from app import views
# from app import error