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
    x = np.linspace(a, b, 10**6)
    y = np.vectorize(value)(f, x)
    sections = np.linspace(a, b, n + 1)
    sec = []
    x_hist = []
    y_hist = []
    for i in range(len(sections)):
        if i < len(sections) - 1:
            sec.append([c := sections[i], d := sections[i + 1]])
            x_hist.append((d + c) / 2)
            y_hist.append(value(f, (d + c) / 2))
        else:
            pass
    calka = sum(y_hist)
    plt.bar(x_hist, y_hist, width=(b - a) / n)
    plt.plot(x, y, color="red")
    plt.grid(True)
    plt.savefig("Technologie Informacyjne\Strona\Strona_Mazi\website\static\\function.png")
    return calka

if __name__ == "__main__":
    ploting(-pi/2, pi/2, 10, f:='cos(x)')