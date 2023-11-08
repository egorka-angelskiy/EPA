from flask import Flask, render_template, request
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
        login = request.form.get('Login')
        password = request.form.get('Password')

        connect = psycopg2.connect(**originall)
        cursor = connect.cursor()
        connect.autocommit = True

        query = f'''select password from "user" where login='{login}' '''
        cursor.execute(query)

        try:
            password_db = cursor.fetchone()[0]
        except TypeError:
            return render_template('auth.html')

        if password_db != password:
            return render_template('auth.html')

        query = f'''select name from "user" where login='{login}' '''
        cursor.execute(query)
        name = cursor.fetchone()[0]
        return render_template(
            'home.html',
            user=name
        )

    return render_template('auth.html')


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        login = request.form.get('Login')
        password = request.form.get('Password')
        name = request.form.get('Name')

        connect = psycopg2.connect(**originall)
        cursor = connect.cursor()
        connect.autocommit = True

        query = f'''select count(*) from "user" where login='{login}' '''
        cursor.execute(query)

        if cursor.fetchone()[0] != 0:
            return render_template('reg.html')

        if not re.fullmatch(r'[A-Za-z0-9]{10,}', password):
            return render_template('reg.html')

        query = f'''insert into "user" (login, password, name) values ('{login}', '{password}', '{name}') '''
        cursor.execute(query)

        return render_template(
            'home.html',
            user=name
        )
        
    return render_template('reg.html')

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