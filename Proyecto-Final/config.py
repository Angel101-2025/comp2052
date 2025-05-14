import os

class Config:
    """
    Configuración general de la aplicación Flask.
    Puede extenderse a diferentes entornos (Desarrollo, Producción, etc.).
    """

    # Clave secreta para proteger sesiones y formularios (CSRF)
    SECRET_KEY = os.environ.get('SECRET_KEY', 'clave-secreta-flask')

    # URI de conexión a la base de datos
    # Reemplazado con el nombre correcto de la base de datos
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL',
        'mysql+pymysql://root:root@localhost/biblioteca_digital_personal'
    )

    # Desactiva el sistema de seguimiento de modificaciones de SQLAlchemy (mejora el rendimiento)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
