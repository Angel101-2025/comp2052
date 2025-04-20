from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user, current_user
from app import app, login_manager
from app.forms import LoginForm
from app.models import User

@login_manager.user_loader
def load_user(user_id):
    # Buscar por ID
    for u in ['admin']:
        user = User.get(u)
        if user and str(user.id) == str(user_id):
            return user
    return None

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.get(form.username.data)
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Bienvenido, ' + user.username)
            return redirect(url_for('dashboard'))
        else:
            flash('Usuario o contraseña incorrecta')
    return render_template('login.html', form=form)

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', user=current_user)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Sesión cerrada')
    return redirect(url_for('login'))
