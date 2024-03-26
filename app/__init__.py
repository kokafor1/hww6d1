from flask import Flask

#create a instance
app = Flask(__name__)

#import routes to the app
from . import routes