import socket
import time
#server
# Create a TCP/IP socket
sock = socket.socket(socket.INET, socket.SOCK_STREAM)

# Connect the socket to the server
server_address = ('server_address', 10000)  # replace 'server_address' with the IP address or hostname of the server
sock.connect(server_address)

# Get the IP address of the client
client_address = sock.getsockname()

# Retry to send the IP address to the server indefinitely
while True:
    try:
        # Send the IP address to the server
        sock.sendall(client_address[0].encode())

        # Receive a response from the server
        received = sock.recv(1024)

        # Print the response
        print(f'Received: {received.decode()}')

        # Break the loop if the server sends an 'exit' message
        if received.decode() == 'exit':
            break

    except Exception as e:
        print(f'Error: {e}')

    # Add a delay between retries
    time.sleep(1)

# Close the socket
sock.close()
