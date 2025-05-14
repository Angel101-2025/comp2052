from app import create_app, db
from app.models import Role, User
from werkzeug.security import generate_password_hash

app = create_app()

with app.app_context():
    roles = ['Admin', 'Moderador', 'Lector']
    for role_name in roles:
        existing_role = Role.query.filter_by(name=role_name).first()
        if not existing_role:
            new_role = Role(name=role_name)
            db.session.add(new_role)
            print(f'✅ Rol "{role_name}" creado.')

    db.session.commit()

    users_data = [
        {
            "username": "Administrador",
            "email": "admin@example.com",
            "password": "admin123",
            "role_name": "Admin"
        },
        {
            "username": "Moderador Uno",
            "email": "mod@example.com",
            "password": "mod123",
            "role_name": "Moderador"
        },
        {
            "username": "Lector Uno",
            "email": "lector@example.com",
            "password": "lector123",
            "role_name": "Lector"
        }
    ]

    for user_info in users_data:
        existing_user = User.query.filter_by(email=user_info['email']).first()
        if not existing_user:
            role = Role.query.filter_by(name=user_info['role_name']).first()
            user = User(
                username=user_info['username'],
                email=user_info['email'],
                role=role
            )
            user.set_password(user_info['password'])
            db.session.add(user)
            print(f'✅ Usuario "{user.username}" creado con rol "{role.name}".')
        else:
            print(f'ℹ️ El usuario con email {user_info["email"]} ya existe.')

    db.session.commit()
    print("✅ Todos los usuarios fueron procesados correctamente.")
