from flask import Flask, render_template, redirect, request, url_for, session, flash, Blueprint, abort


user = Blueprint('/user', __name__)

@user.route('/')
def home_page():
	return render_template('user/home_page.html')


@user.route('/registration')
def registration():

	return render_template('user/reg.html')


@user.route('/authtorization')
def authtorization():

	return render_template('user/auth.html')