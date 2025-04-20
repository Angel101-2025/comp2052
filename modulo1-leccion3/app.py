from flask import Flask, request, jsonify

app = Flask(__name__)

# Almacenamiento en memoria
usuarios = []

# Ruta GET /info
@app.route('/info', methods=['GET'])
def info():
    return jsonify({
        "sistema": "Gestor de Usuarios y Productos",
        "version": "1.0",
        "estado": "Activo"
    })

# Ruta POST /crear_usuario
@app.route('/crear_usuario', methods=['POST'])
def crear_usuario():
    datos = request.get_json()

    if not datos:
        return jsonify({"error": "No se recibió información"}), 400

    nombre = datos.get('nombre')
    correo = datos.get('correo')

    if not nombre or not correo:
        return jsonify({"error": "Faltan campos obligatorios: nombre y/o correo"}), 400

    nuevo_usuario = {
        "id": len(usuarios) + 1,
        "nombre": nombre,
        "correo": correo
    }

    usuarios.append(nuevo_usuario)
    return jsonify({
        "mensaje": "Usuario creado exitosamente",
        "usuario": nuevo_usuario
    }), 201

# Ruta GET /usuarios
@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    return jsonify({
        "cantidad": len(usuarios),
        "usuarios": usuarios
    })

if __name__ == '__main__':
    app.run(debug=True)
