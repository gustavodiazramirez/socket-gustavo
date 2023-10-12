import socket

# Linea para crear un socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Lineas para coonectar al servidor
host = '127.0.0.1'  # La dirección IP del servidor (localhost)
port = 12000     # El puerto en el que el servidor está escuchando
client_socket.connect((host, port))

# Enviar datos al servidor
message = "Hola desde el cliente"
client_socket.send(message.encode('utf-8'))

# Linea para recibir datos del servidor
data = client_socket.recv(1024)  # Aquí se resiven datos del servidor hasta 1024 bytes
print(f"Recibido del servidor: {data.decode('utf-8')}")

# Linea para cerrar el socket del cliente
client_socket.close()
