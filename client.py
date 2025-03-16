import socket

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
host = '127.0.0.1'  # Localhost
port = 12345
client_socket.connect((host, port))

# Receive message from server
message = client_socket.recv(1024).decode()
print(f"Received from server: {message}")

# Close the connection
client_socket.close()
