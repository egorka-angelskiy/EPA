from flask import Flask, render_template, request, redirect, url_for
from data import *
from db import *
import re

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
    if request.method == 'POST':
        login = request.form.get('Логин')
        password = request.form.get('Пароль')

        if Auth(login, password, 'users2'):
            data = Select(login, 'users2')
            col = Columns('users2')

            area = {col[i][0]: data[i] for i in range(len(data))}
            return render_template(
                'home.html'
            )

    return render_template('1auth.html')


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        login = request.form.get('Логин')

        if ExistenceUser(login, 'users2'):
            print(ExistenceUser(login, 'users2'))
            Insert(request.form, 'users2')
            return redirect(url_for('registration2'))

        return render_template('1reg.html')

    return render_template('1reg.html')


@app.route('/registration2', methods=['GET', 'POST'])
def registration2():
    if request.method == 'POST':
        if RegData(request.form):
            RegData(request.form)
            return render_template('home.html')

    return render_template('1reg2.html')

#Каталог с услугами
@app.route('/catalog')
def catalog():
    return render_template('catalog.html')

#Коммунальные услуги
@app.route('/utility_services')
def ut_service():
    return render_template('utility_services.html')

#Жилищные услуги
@app.route('/house_services')
def house_service():
    return render_template(
        'house_services.html',
        service=CAT_HOUSE_SERVE
    )

#Коммуналка(вода)
@app.route('/water')
def ut_water_serve():
    return render_template(
        'water.html',
        service=CAT_UTIL_WATER
    )

#Коммуналка(электричество)
@app.route('/electricity')
def ut_electr_serve():
    return render_template(
        'electricity.html',
        service=CAT_UTIL_ELECTR
    )

#Коммуналка(газ)
@app.route('/gas')
def ut_gas_serve():
    return render_template(
        'gas.html',
        service=CAT_UTIL_GAS
    )