from flask import Flask, render_template, redirect, request, url_for, session, flash, Blueprint
from data import *

service = Blueprint('/service', __name__)


@service.route('/catalog')
def catalog():
    return render_template('service/catalog.html')


@service.route('/utility_services')
def ut_service():
    return render_template('service/utility_services.html')


@service.route('/house_services')
def house_service():
    return render_template(
        'service/house_services.html',
        service=CAT_HOUSE_SERVE
    )


@service.route('/water')
def ut_water_serve():
    return render_template(
        'service/water.html',
        service=CAT_UTIL_WATER
    )


@service.route('/electricity')
def ut_electr_serve():
    return render_template(
        'service/electricity.html',
        service=CAT_UTIL_ELECTR
    )


@service.route('/gas')
def ut_gas_serve():
    return render_template(
        'service/gas.html',
        service=CAT_UTIL_GAS
    )