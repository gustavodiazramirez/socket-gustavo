import socket

# Linea para crear un socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Lineas para enlazar el socket a una dirección y puerto
host = '127.0.0.1'  # La dirección IP (Localhost) en la que el servidor escuchará 
port = 12000       # El puerto en el que el servidor escuchará
server_socket.bind((host, port))

# Línea para comenzar a escuchar conexiones entrantes
server_socket.listen(10)

print(f"Esperando conexiones en {host}:{port}...")

# Linea para aceptar una conexión entrante
client_socket, client_address = server_socket.accept()
print(f"La conexión ha sido establecida desde {client_address}")

# Enviar y recibir datos
data = client_socket.recv(1024)  # Recibir datos del cliente (hasta 1024 bytes)
print(f"Recibido: {data.decode('utf-8')}")

# Línea para enviar una respuesta al cliente
response = "¡HOLA DESDE EL SERVIDOR!"
client_socket.send(response.encode('utf-8'))

# Línea para cerrar los sockets
server_socket.close()
