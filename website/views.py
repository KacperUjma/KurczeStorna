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
    if f is None:
        return None
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
    calka = sum(y_hist)
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
        n = request.form.get("slider")
        print(n)
    if '+' in request.form:
        funkcja += '+'
        return render_template('main.html',funkcja = funkcja)
    elif '-' in request.form:
        funkcja += '-'
        return render_template('main.html',funkcja = funkcja)
    elif '*' in request.form:
        funkcja += '*'
        return render_template('main.html',funkcja = funkcja)
    elif '/' in request.form:
        funkcja += '/'
        return render_template('main.html',funkcja = funkcja)
    elif 'sqrt' in request.form:
        funkcja += 'sqrt'
        return render_template('main.html',funkcja = funkcja)
    elif '^' in request.form:
        funkcja += '^'
        return render_template('main.html',funkcja = funkcja)
    elif 'sin' in request.form:
        funkcja += 'sin'
        return render_template('main.html',funkcja = funkcja)
    elif 'cos' in request.form:
        funkcja += 'cos'
        return render_template('main.html',funkcja = funkcja)
    elif 'tan' in request.form:
        funkcja += 'tan'
        return render_template('main.html',funkcja = funkcja)
    elif 'ctan' in request.form:
        funkcja += 'ctan'
        return render_template('main.html',funkcja = funkcja)
    elif 'x' in request.form:
        funkcja += 'x'
        return render_template('main.html',funkcja = funkcja)
    elif '(' in request.form:
        funkcja += '('
        return render_template('main.html',funkcja = funkcja)
    elif ')' in request.form:
        funkcja += ')'
        return render_template('main.html',funkcja = funkcja)
    elif 'draw' in request.form:
        print(funkcja)
        print(ploting(0.01,100,1000,funkcja))
        return render_template('main.html',funkcja = funkcja)
    elif 'clear' in request.form:
        funkcja = ""
        return render_template('main.html',funkcja = funkcja)
    return render_template('main.html',funkcja=funkcja)
