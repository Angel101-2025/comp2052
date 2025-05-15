
from flask import Blueprint, request, jsonify
from app.models import db, LibroPersonal  

# Blueprint de prueba para libros personales
main = Blueprint('test_routes', __name__, url_prefix='/api-test')

@main.route('/')
@main.route('/dashboard')
def index():
    """
    Página de inicio pública (home).
    """
    return '<h1>Corriendo en Modo de Prueba: Biblioteca Digital Personal</h1>'


@main.route('/libros', methods=['GET'])
def listar_libros():
    """
    Retorna una lista de libros personales (JSON).
    """
    libros = LibroPersonal.query.all()

    data = [
        {
            'id': libro.id,
            'titulo': libro.titulo,
            'autor': libro.autor,
            'genero': libro.genero,
            'anio_publicacion': libro.anio_publicacion,
            'url': libro.url,
            'notas': libro.notas,
            'etiquetas': libro.etiquetas,
            'usuario_id': libro.usuario_id
        }
        for libro in libros
    ]
    return jsonify(data), 200


@main.route('/libros/<int:id>', methods=['GET'])
def obtener_libro(id):
    """
    Retorna un libro personal por su ID (JSON).
    """
    libro = LibroPersonal.query.get_or_404(id)

    data = {
        'id': libro.id,
        'titulo': libro.titulo,
        'autor': libro.autor,
        'genero': libro.genero,
        'anio_publicacion': libro.anio_publicacion,
        'url': libro.url,
        'notas': libro.notas,
        'etiquetas': libro.etiquetas,
        'usuario_id': libro.usuario_id
    }

    return jsonify(data), 200


@main.route('/libros', methods=['POST'])
def crear_libro():
    """
    Crea un libro personal sin validación.
    Espera JSON con los campos necesarios.
    """
    data = request.get_json()

    if not data:
        return jsonify({'error': 'No se proporcionaron datos'}), 400

    libro = LibroPersonal(
        titulo=data.get('titulo'),
        autor=data.get('autor'),
        genero=data.get('genero'),
        anio_publicacion=data.get('anio_publicacion'),
        url=data.get('url'),
        notas=data.get('notas'),
        etiquetas=data.get('etiquetas'),
        usuario_id=data.get('usuario_id')
    )

    db.session.add(libro)
    db.session.commit()

    return jsonify({'message': 'Libro creado', 'id': libro.id}), 201


@main.route('/libros/<int:id>', methods=['PUT'])
def actualizar_libro(id):
    """
    Actualiza un libro personal sin validación de usuario.
    """
    libro = LibroPersonal.query.get_or_404(id)
    data = request.get_json()

    libro.titulo = data.get('titulo', libro.titulo)
    libro.autor = data.get('autor', libro.autor)
    libro.genero = data.get('genero', libro.genero)
    libro.anio_publicacion = data.get('anio_publicacion', libro.anio_publicacion)
    libro.url = data.get('url', libro.url)
    libro.notas = data.get('notas', libro.notas)
    libro.etiquetas = data.get('etiquetas', libro.etiquetas)

    db.session.commit()

    return jsonify({'message': 'Libro actualizado', 'id': libro.id}), 200


@main.route('/libros/<int:id>', methods=['DELETE'])
def eliminar_libro(id):
    """
    Elimina un libro personal.
    """
    libro = LibroPersonal.query.get_or_404(id)
    db.session.delete(libro)
    db.session.commit()

    return jsonify({'message': 'Libro eliminado', 'id': libro.id}), 200

