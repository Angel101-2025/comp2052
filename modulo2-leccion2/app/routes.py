from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import RegistrationForm

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Aquí guardarías los datos del usuario
        flash('¡Registro exitoso!', 'success')
        return redirect(url_for('register'))
    return render_template('register.html', form=form)

