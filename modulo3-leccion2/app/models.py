from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

# Simulación de base de datos
users = {
    'admin': {
        'id': 1,
        'username': 'admin',
        'password': generate_password_hash('admin123'),
        'role': 'admin'
    },
    'editor': {
        'id': 2,
        'username': 'editor',
        'password': generate_password_hash('editor123'),
        'role': 'editor'
    },
    'viewer': {
        'id': 3,
        'username': 'viewer',
        'password': generate_password_hash('viewer123'),
        'role': 'viewer'
    }
}

class User(UserMixin):
    def __init__(self, id, username, password, role):
        self.id = id
        self.username = username
        self.password = password
        self.role = role

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @staticmethod
    def get(username):
        user = users.get(username)
        if not user:
            return None
        return User(user['id'], username, user['password'], user['role'])
