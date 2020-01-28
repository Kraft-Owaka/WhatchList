from flask import Flask
from .config import DevConfig

# Initializing application
app = Flask(__name__,instance_relative_config = True)

#Setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

from app import views

#We import the Flask class 
# from flask module and 
# use it to create an app 
# instance. We pass in the 
# __name__ variable.