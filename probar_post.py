import requests

# 1. Probar GET /info
url_info = 'http://127.0.0.1:5000/info'
respuesta_info = requests.get(url_info)

print("📘 GET /info")
print("Código de estado:", respuesta_info.status_code)
print("Respuesta JSON:", respuesta_info.json())
print("\n" + "-"*40 + "\n")

# 2. Probar POST /mensaje
url_mensaje = 'http://127.0.0.1:5000/mensaje'
datos = {
    'mensaje': 'Este es un mensaje de prueba desde Python'
}

respuesta_post = requests.post(url_mensaje, json=datos)

print("📨 POST /mensaje")
print("Código de estado:", respuesta_post.status_code)
print("Respuesta JSON:", respuesta_post.json())
