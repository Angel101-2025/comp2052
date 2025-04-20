from flask import Flask, request, jsonify

app = Flask(__name__)

# Ruta GET /info
@app.route('/info', methods=['GET'])
def info():
    return jsonify({
        'nombre': 'Servidor Flask de Ejemplo',
        'version': '1.0',
        'descripcion': 'Este servidor responde a solicitudes GET y POST.'
    })

# Ruta POST /mensaje
@app.route('/mensaje', methods=['POST'])
def mensaje():
    datos = request.get_json()

    if not datos or 'mensaje' not in datos:
        return jsonify({'error': 'No se recibió un mensaje válido'}), 400

    mensaje_usuario = datos['mensaje']
    respuesta = f"Hola, recibí tu mensaje: '{mensaje_usuario}'"

    return jsonify({
        'respuesta': respuesta,
        'original': mensaje_usuario
    })

if __name__ == '__main__':
    app.run(debug=True)
