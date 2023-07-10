from flask import Blueprint, render_template, request
from website import ploting, value

views = Blueprint('views',__name__)

@views.route('/',methods = ['GET','POST'])
def home():
    global funkcja
    funkcja = "2*x^2-x+1"
    if request.method == 'POST':
        funkcja = request.form.get("funkcja")
    if '+' in request.form:
        funkcja += '+'
        return render_template('Home.html',funkcja = funkcja)
    elif '-' in request.form:
        funkcja += '-'
        return render_template('Home.html',funkcja = funkcja)
    elif '*' in request.form:
        funkcja += '*'
        return render_template('Home.html',funkcja = funkcja)
    elif '/' in request.form:
        funkcja += '/'
        return render_template('Home.html',funkcja = funkcja)
    elif 'sqrt' in request.form:
        funkcja += 'sqrt'
        return render_template('Home.html',funkcja = funkcja)
    elif '^' in request.form:
        funkcja += '^'
        return render_template('Home.html',funkcja = funkcja)
    elif 'sin' in request.form:
        funkcja += 'sin'
        return render_template('Home.html',funkcja = funkcja)
    elif 'cos' in request.form:
        funkcja += 'cos'
        return render_template('Home.html',funkcja = funkcja)
    elif 'tan' in request.form:
        funkcja += 'tan'
        return render_template('Home.html',funkcja = funkcja)
    elif 'ctan' in request.form:
        funkcja += 'ctan'
        return render_template('Home.html',funkcja = funkcja)
    elif 'x' in request.form:
        funkcja += 'x'
        return render_template('Home.html',funkcja = funkcja)
    elif '(' in request.form:
        funkcja += '('
        return render_template('Home.html',funkcja = funkcja)
    elif ')' in request.form:
        funkcja += ')'
        return render_template('Home.html',funkcja = funkcja)
    elif 'draw' in request.form:
        print(funkcja)
        wartosc = ploting(-3,3,10,funkcja)
        print(wartosc)
        return render_template('Home.html',funkcja = funkcja)
    return render_template('Home.html',funkcja=funkcja)
