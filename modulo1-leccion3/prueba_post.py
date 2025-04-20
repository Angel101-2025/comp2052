import requests



url = 'http://127.0.0.1:5000/crear_usuario'

usuario = {
    'nombre': 'María Gómez',
    'correo': 'maria@example.com'
}

respuesta = requests.post(url, json=usuario)

print("Código de estado:", respuesta.status_code)
print("Respuesta del servidor:", respuesta.json())
