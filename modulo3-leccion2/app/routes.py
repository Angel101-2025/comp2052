from flask import render_template, redirect, url_for, flash, request
from flask_login import (
    login_user, logout_user, login_required,
    current_user
)
from flask_principal import (
    Identity, identity_loaded, RoleNeed,
    UserNeed, identity_changed, AnonymousIdentity,
    Permission
)
from app import app, login_manager
from app.forms import LoginForm
from app.models import User

# 🔐 Definir permisos por roles
admin_permission = Permission(RoleNeed('admin'))
editor_permission = Permission(RoleNeed('editor'))


# Cargar usuario desde ID

@login_manager.user_loader
def load_user(user_id):
    # Buscar entre los usuarios simulados
    for username in ['admin', 'editor', 'viewer']:
        user = User.get(username)
        if user and str(user.id) == str(user_id):
            return user
    return None

# Ruta pública

@app.route('/')
def index():
    return render_template('base.html')


# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.get(form.username.data)
        if user and user.check_password(form.password.data):
            login_user(user)

            # Activar Flask-Principal
            identity_changed.send(app, identity=Identity(user.id))

            flash(f'Bienvenido, {user.username}')
            return redirect(url_for('dashboard'))
        else:
            flash('Usuario o contraseña incorrecta')
    return render_template('login.html', form=form)


# Dashboard privado
@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', user=current_user)


# Ruta protegida: solo admin

@app.route('/admin-only')
@login_required
@admin_permission.require(http_exception=403)
def admin_only():
    return "<h2>✅ Vista solo para admins.</h2>"


# Ruta protegida: solo editores

@app.route('/edit')
@login_required
@editor_permission.require(http_exception=403)
def edit_content():
    return "<h2>✅ Vista de edición para editores.</h2>"


# Logout

@app.route('/logout')
@login_required
def logout():
    logout_user()

    # Informar a Flask-Principal
    identity_changed.send(app, identity=AnonymousIdentity())

    flash('Sesión cerrada correctamente')
    return redirect(url_for('login'))


# Cargar identidad y roles al iniciar sesión
@identity_loaded.connect_via(app)
def on_identity_loaded(sender, identity):
    user = current_user
    if not user.is_authenticated:
        return

    identity.user = user
    identity.provides.add(UserNeed(user.id))
    identity.provides.add(RoleNeed(user.role))
