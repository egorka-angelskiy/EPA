from flask import Flask, render_template, redirect, request, url_for, session, flash, Blueprint
from db import *
from functions import *
import jwt
import random
from pprint import *

user = Blueprint('/user', __name__)

@user.route('/')
def home():
    # print(session)
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
        
        query = f"""select count(*) from home where login='{login}'"""
        cursor.execute(query)
        number = cursor.fetchone()[0]
        insert_reg(request.form, login, number + 1)
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

            query = f"""select * from home where login='{info[1]}';"""
            cursor.execute(query)
            a = cursor.fetchall()
            info = info[3:]
            
            c = {get_col('home')[2:][i][0]: [] for i in range(len(get_col('home')[2:]))}
            counter_row = len(a)
            number_home = []
            for i in range(counter_row):
                for j in range(len(get_col('home')[2:])):
                    tmp = a[i][2:]
                    c[get_col('home')[2:][j][0]] += [tmp[j]]
                number_home += [a[i][0]]
                               

            
            return render_template(
                'user/profile.html',
                user={get_col('users')[3:][i][0]: info[i] for i in range(len(info))},
                data=c,
                n=counter_row,
                number_home=number_home
            )
            
    return redirect(url_for('/user.authurization'))

@user.route('/update', methods=['POST', 'GET'])
def update():
    if request.method == 'POST':
        query = f"""select login from users where id='{session['id']}'"""
        cursor.execute(query)        
        login = cursor.fetchone()[0]
        number = request.form['button']
        update_home(request.form, login, number)
        
    return redirect(url_for('/user.profile'))

@user.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        
        query = f"""select login from users where id='{session['id']}'"""
        cursor.execute(query)
        login = cursor.fetchone()[0]
        
        query = f"""select count(*) from home where login='{login}'"""
        cursor.execute(query)
        number = cursor.fetchone()[0] + 1
        
        
        insert_reg(request.form, login, number)
    return redirect(url_for('/user.profile'))

@user.route('/delete', methods=['POST', 'GET'])
def delete():
    if request.method == 'POST':
        query = f"""select login from users where id='{session['id']}'"""
        cursor.execute(query)        
        login = cursor.fetchone()[0]
        number = request.form['button']
        
        query = f"""delete from "home" where login='{login}' and number='{number}'"""
        cursor.execute(query)
        
    return redirect(url_for('/user.profile'))
    

@user.route('/token', methods=['POST', 'GET'])
def token():
    if 'log' in session:
        query = f"""select * from users where id='{session['id']}'"""
        cursor.execute(query)
        user = cursor.fetchone()
        
        query = f"""select * from home where login='{user[1]}'"""
        cursor.execute(query)
        home = cursor.fetchone()    
        

        token = jwt.encode(
            payload={
                (get_col('users') + get_col('home'))[i][0]: (user + home)[i] for i in range(len((user + home)))
                },
            key=str(random.randint(0, 10))
        )
        
        # https://jwt.io/
        return token
    return redirect(url_for('/user.authurization'))
