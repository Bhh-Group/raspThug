import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address given on the command line
server_address = ('', 10000)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()

    try:
        # Receive the IP address from the client
        received = connection.recv(1024)
        client_ip = received.decode()

        # Send a response to the client
        connection.sendall(f"Your IP address is: {client_ip}".encode())

    finally:
        # Close the connection
        connection.close()
