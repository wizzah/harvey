from flask import Flask, render_template, redirect, url_for, request, session, flash
from functools import wraps
from flask.ext.pymongo import PyMongo
from pymongo import Connection

app = Flask(harvey)

app.secret_key = "my precious"

mongo = PyMongo(app)

@app.route('/')
def home_page():
    online_users = mongo.db.users.find({'online': True})
    return render_template('index.html',
        online_users=online_users)








def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to log in first.')
            return redirect(url_for('login'))
    return wrap

@app.route('/welcome')
def welcome():
    # return render_template("welcome.html")
    return render_template("index.html")

@app.route('/form')
def form():
    # return render_template("form.html")
    return render_template("form.html")



@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True
            flash('You were just logged in!')
            return redirect(url_for('welcome'))
    return render_template('login.html', error=error)

@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You were just logged out!')
    return redirect(url_for('welcome'))

if __name__ == '__main__':
    app.run(debug=True)
