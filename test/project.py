from user import *

from flask import Flask, render_template, redirect, request, url_for, session, flash, Blueprint


app = Flask(__name__)
app.register_blueprint(user)