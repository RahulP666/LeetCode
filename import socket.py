import socket

def get_local_ip():
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        # Connect to a remote server (doesn't actually connect, just initializes the socket)
        s.connect(('8.8.8.8', 80))
        # Get the local IP address
        local_ip = s.getsockname()[0]
    finally:
        # Close the socket
        s.close()

    return local_ip

# Get the local IP address
ip_address = get_local_ip()
print("Local IP address:", ip_address)
