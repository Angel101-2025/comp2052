from flask import Flask
from flask_login import LoginManager
from flask_principal import Principal

app = Flask(__name__)
app.config['SECRET_KEY'] = 'una_clave_segura'

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

principals = Principal(app)

from app import routes
