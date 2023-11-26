from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)

app.secret_key = 'termin123'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '213ll1$M@'
app.config['MYSQL_DB'] = 'corefizik_fitness'

mysql = MYSQL(app)

@app.route('/')
@app.route('/login' , methods=['GET', 'POST'])
def login():
    msg=''
    if request.method == 'POST' and 'login_id' in request.form and 'login_role_id' in request.formand 'login_username' in request.form and 'user_password' in request.form:
        login_id=request.form['login_id']
        login_role_id=request.form['login_role_id']
        login_username=request.form['login_username']
        user_password=request.form['user_password']
        cursor=mysql.connection.cursor(MYSQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM corefizik_fitness WHERE login_id=%s AND login_role_id=%s AND login_username=%s AND user_password=%s', (login_id, login_role_id, login_username, user_password))
        account=cursor.fetchone()
        if account:
            session['loggedin']=True
            session['id']=account['id']
            session['username']=account['username']
            msg='Logged in successfully!'
            return render_template('index.html', msg=msg)
        else:
            msg='Incorrect loginid/password!'
    return render_template('login.html, msg=msg')

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for(login))

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    msg=''
    if request.method == 'POST' and 'login_id' in request.form and 'login_role_id' in request.form and 'login_username' in request.form and 'user_password' in request.form:
        login_id=request.form['login_id']
        login_role_id=request.form['login_role_id']
        login_username=request.form['login_username']
        user_password=request.form['user_password']
        cursor=mqsql.connection.cursor(MYSQLdb.cursor.DictCursor)
        cursor.execute('SELECT * FROM corefizik_fitness WHERE loginid=%s', (login_id,))
        account=cursor.fetchnone()
        if account:
            msg='Login not successful!'
        elif not re.match(r'[A-Za-z0-9]+', login_id):
            msg='Username must only contain characters and numbers!'
        elif not login_id or login_role_id or login_username or user_password:
            msg='Please fill out the form!'
        else:
            cursor.execute('INSERT INTO corefizik_fitness VALUES (NULL, %s, %s)', login_id, login_role_id, login_username, user_password)
            mysql.connection.commit()
            msg='You have successfully logged in!'
    elif request.method=='POST'
        msg='Please fill out the form!'
    return render_template('profile.html', msg=msg)
