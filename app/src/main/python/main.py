import socket

# Configura el servidor
host = "0.0.0.0"  # Escucha en todas las interfaces de red
port = 10000     # Puerto en el que escuchará el servidor

# Crea un socket TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlaza el socket al host y puerto especificados
server_socket.bind((host, port))

# Escucha conexiones entrantes (máximo 1)
server_socket.listen(1)

print(f"Servidor escuchando en {host}:{port}")

# Acepta una conexión entrante
client_socket, client_address = server_socket.accept()
print(f"Conexión establecida desde {client_address}")

# Maneja la conexión entrante
# while True:
#     data = client_socket.recv(1024)  # Recibe datos (hasta 1024 bytes)
#     if not data:
#         break  # Si no hay datos, termina el bucle
#     received_data = data.decode("utf-8")
#     print(f"Datos recibidos: {received_data}")

while True:
    data = client_socket.recv(1024)  # Recibe datos (hasta 1024 bytes)
    if data:
        if data.decode("utf-8") == 'END':
            break  # Si no hay datos, termina el bucle        
        else:
            received_data = data.decode("utf-8")
            print(f"Datos recibidos: {received_data}")

# Cierra la conexión con el cliente
client_socket.close()

# Cierra el socket del servidor
server_socket.close()