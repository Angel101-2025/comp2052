from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm password', validators=[DataRequired(), EqualTo('password')])
    role = SelectField('Role', choices=[('Lector', 'Lector'), ('Moderador', 'Moderador')], validators=[DataRequired()])
    submit = SubmitField('Register')

class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Current password', validators=[DataRequired()])
    new_password = PasswordField('New password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm new password', validators=[DataRequired(), EqualTo('new_password')])
    submit = SubmitField('Update Password')

class LibroForm(FlaskForm):
    titulo = StringField('Title', validators=[DataRequired()])
    autor = StringField('Author')
    genero = StringField('Genre')
    anio_publicacion = StringField('Year')
    url = StringField('Link (optional)')
    notas = TextAreaField('Notes')
    etiquetas = StringField('Tags (comma-separated)')
    submit = SubmitField('Save')