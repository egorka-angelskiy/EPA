from flask import Flask, render_template, redirect, request, url_for, session, flash, Blueprint
from db import *
from functions import *

user = Blueprint('/user', __name__)

@user.route('/')
def home():
    print(session)
    return render_template('user/home.html')

@user.route('/registration', methods=['POST', 'GET'])
def registration():
    if not session:
        if request.method == 'POST':
            login = request.form.get('login')
            password = request.form.get('password')
            
            if '' in [login, password]:
                return render_template('user/reg.html')
            
            if check_exists_user(login):
                return render_template('user/reg.html')
            
            if not check_password(password):
                return render_template('user/reg.html')
                
            query = f"""insert into users (login, password) values ('{login}', '{password}')"""
            cursor.execute(query)
            
            query = f"""select id from users where login='{login}'"""
            cursor.execute(query)
            id = cursor.fetchone()[0]
                
            session['log'] = True
            session['id'] = id
            
            return redirect(url_for('/user.registration2'))
        return render_template('user/reg.html')
    
    return render_template('user/home.html')


@user.route('/registration2', methods=['POST', 'GET'])
def registration2():
    if request.method == 'POST':
        update_reg(request.form, session['id'])
        return redirect(url_for('/user.registration3'))
    return render_template('user/reg2.html')


@user.route('/registration3', methods=['POST', 'GET'])
def registration3():
    if request.method == 'POST':
        query = f"""select login from users where id='{session['id']}'"""
        cursor.execute(query)
        login = cursor.fetchone()[0]
        insert_reg(request.form, login)
        return render_template(
            'user/choose.html',
            version='зарегистриоровались'
        )
    return render_template('user/reg3.html')



@user.route('/authurization', methods=['POST', 'GET'])
def authurization():
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        
        query = f"""select password, id from users where login='{login}'"""
        cursor.execute(query)
        
        db_password, id = cursor.fetchone()
        if password != db_password:
            print('Error password')
            return render_template('user/auth.html')
        
        session['id'] = id
        session['log'] = True
        
        return render_template(
            'user/choose.html',
            version='вошли в свой аккаунт'
        )
    return render_template('user/auth.html')


@user.route('/logout')
def logout():
   session.clear()
   return redirect(url_for('/user.home'))


@user.route('/profile', methods=['POST', 'GET'])
def profile():
    if 'log' in session:
        if session['log']:
            query = f"""select * from users where id={session['id']}"""
            cursor.execute(query)
            info = cursor.fetchone()
            
            query = f"""select * from home  where login='{info[2]}';"""
            cursor.execute(query)
            data = info[3:] + cursor.fetchone()[1:]
            
            col = get_col('users')[3:] + get_col('home')[1:]
        
            area = {col[i][0]: data[i] for i in range(len(data))}
            return render_template(
                'user/profile.html',
                data=area
            )
            
        if request.method == 'POST':
            print(1)
            
    return redirect(url_for('/user.authurization'))