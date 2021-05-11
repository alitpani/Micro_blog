from flask_login.utils import login_user, logout_user
from app import app
from flask_login import login_user,current_user,logout_user
from flask import render_template,flash,redirect,url_for
from app.forms import LoginForm
from app.models import User

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'miguel'}

    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]


    return render_template('index.html',title = 'Home', user = user,posts = posts )


@app.route('/2')
def secondpage():
   return '<H1>second page </H1>'

@app.route('/login',methods = ['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        # flash('Login req for user {} , remember_me {}'.format(form.username.data,form.remember_me.data))
        user = User.query.filter_by(username = form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid Username or Password')
            return redirect(url_for('login'))
        
        login_user(user,remember=form.remember_me.data)

        return redirect(url_for('index'))
    return render_template('login.html',title = 'Sign_In',form = form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

