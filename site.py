from flask import Flask, render_template, request
from data import *

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('main.html')


@app.route('/home')
def home():
    return render_template(
        'home.html',
        user='Egor'
    )


@app.route('/authorization', methods=['GET', 'POST'])
def authorization():
    return render_template('auth.html')


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    return render_template('reg.html')


@app.route('/catalog')
def catalog():
    return render_template(
        'catalog.html',
        info=CATALOG
    )


if __name__ == '__main__':
    app.run(debug=True, port=8080)
