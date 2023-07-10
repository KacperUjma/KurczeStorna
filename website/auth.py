from flask import Blueprint
from flask import render_template

auth = Blueprint('auth',__name__)

@auth.route('/about')
def about():
    return render_template("about.html")

@auth.route('/authors')
def authors():
    return render_template('authors.html')

@auth.route('/project')
def project():
    return render_template("project.html")