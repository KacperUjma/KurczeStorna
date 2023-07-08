from flask import Blueprint

auth = Blueprint('auth',__name__)

@auth.route('/about')
def about():
    return "about"

@auth.route('/authors')
def authors():
    return "authors"

@auth.route('/project')
def project():
    return "project"