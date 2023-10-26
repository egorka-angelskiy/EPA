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
    return render_template('catalog.html')

@app.route('/utility_services')
def ut_service():
    return render_template('utility_services.html')

@app.route('/house_services')
def hous_service():
    return render_template(
        'house_services.html',
        info = CAT_HOUSE_SERVE
        )


@app.route('/water')
def ut_water_serve():
    return render_template(
        'water.html',
        info = CAT_UTIL_WATER
    )
    
@app.route('/electricity')
def ut_electr_serve():
    return render_template(
        'electricity.html',
        info = CAT_UTIL_ELECTR
    )
    
@app.route('/gas')
def ut_gas_serve():
    return render_template(
        'gas.html',
        info = CAT_UTIL_GAS
    )

if __name__ == '__main__':
    app.run(debug=True, port=8080)
