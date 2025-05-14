from app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    role = db.relationship('Role', backref='users')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class LibroPersonal(db.Model):
    __tablename__ = 'libro_personal'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150), nullable=False)
    autor = db.Column(db.String(100))
    genero = db.Column(db.String(50))
    anio_publicacion = db.Column(db.Integer)
    url = db.Column(db.String(255))
    notas = db.Column(db.Text)
    etiquetas = db.Column(db.String(255))
    usuario_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    usuario = db.relationship('User', backref='libros')