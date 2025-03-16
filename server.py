import socket

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to an IP and port
host = '127.0.0.1'  # Localhost
port = 12345
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(5)
print(f"Server is listening on {host}:{port}")

# Accept client connection
client_socket, client_address = server_socket.accept()
print(f"Connection established with {client_address}")

# Send message to client
message = "Hello, Client! This is the server."
client_socket.send(message.encode())

# Close the connection
client_socket.close()
server_socket.close()
