from flask import Flask, render_template

app = Flask(__name__)

@app.get('/login')
def login_get():
    return render_template('login.html')

@app.post('/login')
def login_post():
    return 'login post'