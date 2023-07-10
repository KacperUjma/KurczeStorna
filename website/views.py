from flask import Blueprint, render_template, request
from math import sqrt, exp, pi, e, sin, cos, tan
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import os
import threading
matplotlib.use('agg')


views = Blueprint('views',__name__)

symbols = ['x', '+', '-', '*', '/', '^', 'sqrt', '(', ')', 'sin', 'cos', 'tg', 'ctg']
def value(f, x_value):
    for x in symbols:
        if x not in symbols:
            return KeyError("Zle wpisany ciag znakow")
    f = f.replace('^', '**')
    f = f.replace('ctan', '1/tan')
    x = x_value
    try: value = eval(f)
    except: value = None
    return value

def ploting(a, b, n, f):
    x = np.linspace(a, b, 10*5)
    y = np.vectorize(value)(f, x)
    calka = 0
    sections = np.linspace(a, b, n + 1)
    sec = []
    x_hist = []
    y_hist = []
    plt.clf()
    for i in range(len(sections)):
        if i < len(sections) - 1:
            sec.append([c := sections[i], d := sections[i + 1]])
            x_hist.append((d + c) / 2)
            y_hist.append(value(f, (d + c) / 2))
        else:
            pass
    for i in range(len(y_hist)):
        calka += y_hist[i]*((b-a)/n)
    plt.bar(x_hist, y_hist, width=(b-a)/n)
    plt.plot(x, y, color="red")
    plt.grid(True)
    plt.savefig("Technologie Informacyjne\Strona\Strona_Mazi\website\static\\function.png")
    return round(abs(calka),5)

@views.route('/',methods = ['GET','POST'])
def home():
    global funkcja 
    funkcja = "2*x^2-x+1"
    if request.method == 'POST':
        funkcja = request.form.get("funkcja")
        n = int(request.form.get("n"))
        if n <= 0:
            n=1
        print(n)
    if '+' in request.form:
        funkcja += '+'
        return render_template('main.html',funkcja = funkcja,n=n)
    elif '-' in request.form:
        funkcja += '-'
        return render_template('main.html',funkcja = funkcja,n=n)
    elif '*' in request.form:
        funkcja += '*'
        return render_template('main.html',funkcja = funkcja,n=n)
    elif '/' in request.form:
        funkcja += '/'
        return render_template('main.html',funkcja = funkcja,n=n)
    elif 'sqrt' in request.form:
        funkcja += 'sqrt'
        return render_template('main.html',funkcja = funkcja,n=n)
    elif '^' in request.form:
        funkcja += '^'
        return render_template('main.html',funkcja = funkcja,n=n)
    elif 'sin' in request.form:
        funkcja += 'sin'
        return render_template('main.html',funkcja = funkcja,n=n)
    elif 'cos' in request.form:
        funkcja += 'cos'
        return render_template('main.html',funkcja = funkcja,n=n)
    elif 'tan' in request.form:
        funkcja += 'tan'
        return render_template('main.html',funkcja = funkcja,n=n)
    elif 'ctan' in request.form:
        funkcja += 'ctan'
        return render_template('main.html',funkcja = funkcja,n=n)
    elif 'x' in request.form:
        funkcja += 'x'
        return render_template('main.html',funkcja = funkcja,n=n)
    elif '(' in request.form:
        funkcja += '('
        return render_template('main.html',funkcja = funkcja,n=n)
    elif ')' in request.form:
        funkcja += ')'
        return render_template('main.html',funkcja = funkcja,n=n)
    elif 'draw' in request.form:
        print(ploting(-2,2,100,funkcja))
        return render_template('main.html',funkcja = funkcja,n=n)
    elif 'clear' in request.form:
        funkcja = ""
        return render_template('main.html',funkcja = funkcja,n=n)
    return render_template('main.html',funkcja=funkcja)
