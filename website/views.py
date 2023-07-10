from flask import Blueprint, render_template, request
from math import sqrt, exp, pi, e, sin, cos, tan
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from PIL import Image
matplotlib.use('agg')


views = Blueprint('views',__name__)

symbols = ['x', '+', '-', '*', '/', '^', 'sqrt', '(', ')', 'sin', 'cos', 'tg', 'ctg']
def value(f, x_value):
    for x in symbols:
        if x not in symbols:
            return None
    f = f.replace('^', '**')
    f = f.replace('ctan', '1/tan')
    x = x_value
    try: value = eval(f)
    except: value = 0
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
    return round(calka,5)

@views.route('/',methods = ['GET','POST'])
def home():
    global funkcja, a, b, n, plot
    funkcja = "2*x^2-x+1"
    plot = "static\\function_empty.png"
    a, b, n, result = -1, 1, 10, 0
    # print(a,b,n,result)
    if request.method == 'POST':
        funkcja = request.form.get("funkcja")
        try: 
            n = int(request.form.get("n"))
            a = float(request.form.get("a"))
            b = float(request.form.get("b"))
        except: 
            n = 1
            a = 0
            b = 0 
        if n <= 0:
            n=1
        if a>b:
            a=b
        # print("n =",n)
    if '+' in request.form:
        funkcja += '+'
        return render_template('main.html',funkcja = funkcja,n=n,a=a,b=b,result=result,plot=plot)
    elif '-' in request.form:
        funkcja += '-'
        return render_template('main.html',funkcja = funkcja,n=n,a=a,b=b,result=result,plot=plot)
    elif '*' in request.form:
        funkcja += '*'
        return render_template('main.html',funkcja = funkcja,n=n,a=a,b=b,result=result,plot=plot)
    elif '/' in request.form:
        funkcja += '/'
        return render_template('main.html',funkcja = funkcja,n=n,a=a,b=b,result=result,plot=plot)
    elif 'sqrt' in request.form:
        funkcja += 'sqrt'
        return render_template('main.html',funkcja = funkcja,n=n,a=a,b=b,result=result,plot=plot)
    elif '^' in request.form:
        funkcja += '^'
        return render_template('main.html',funkcja = funkcja,n=n,a=a,b=b,result=result,plot=plot)
    elif 'sin' in request.form:
        funkcja += 'sin'
        return render_template('main.html',funkcja = funkcja,n=n,a=a,b=b,result=result,plot=plot)
    elif 'cos' in request.form:
        funkcja += 'cos'
        return render_template('main.html',funkcja = funkcja,n=n,a=a,b=b,result=result,plot=plot)
    elif 'tan' in request.form:
        funkcja += 'tan'
        return render_template('main.html',funkcja = funkcja,n=n,a=a,b=b,result=result,plot=plot)
    elif 'ctan' in request.form:
        funkcja += 'ctan'
        return render_template('main.html',funkcja = funkcja,n=n,a=a,b=b,result=result,plot=plot)
    elif 'x' in request.form:
        funkcja += 'x'
        return render_template('main.html',funkcja = funkcja,n=n,a=a,b=b,result=result,plot=plot)
    elif 'back' in request.form:
        if len(funkcja) > 0:
            funkcja = funkcja[:-1]
        return render_template('main.html',funkcja = funkcja,n=n,a=a,b=b,result=result,plot=plot)
    elif '(' in request.form:
        funkcja += '('
        return render_template('main.html',funkcja = funkcja,n=n,a=a,b=b,result=result,plot=plot)
    elif ')' in request.form:
        funkcja += ')'
        return render_template('main.html',funkcja = funkcja,n=n,a=a,b=b,result=result,plot=plot)
    elif 'draw' in request.form:
        result = ploting(a,b,n,funkcja)
        plot = "static\\function.png"
        return render_template('main.html',funkcja = funkcja,n=n,a=a,b=b,result=result,plot=plot)
    elif 'clear' in request.form:
        a,b,n,result,funkcja = "","","","",""
        plot = "static\\function_empty.png"
        return render_template('main.html',funkcja = funkcja,n=n,a=a,b=b,result=result,plot=plot)
    return render_template('main.html',funkcja = funkcja,n=n,a=a,b=b,result=result,plot=plot)
