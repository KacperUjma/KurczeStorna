from flask import Flask
from math import sqrt, exp, pi, e, sin, cos, tan
import matplotlib.pyplot as plt
import numpy as np

def create_app():
    app = Flask(__name__)

    from .views import views
    from .auth import auth 
    
    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')   
    return app