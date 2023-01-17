import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65000 # Port to listen on (non-privileged ports are > 1023)


# The address family and socket type. "AF_INET" is the Internet address family for IPv4.
# SOCK_STREAM is the socket type for TCP, the protocol that will be used to transport messages in the network.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.bind((HOST, PORT)) # Used to asscoiate a socket to a specific network interface & port

    s.listen() # enables a server to accept connections. It turns a socket to listening mode

    conn, addr = s.accept() # this method blocks execution and waits for an incoming connection.
    # When a client connects, it returns a new socket object representing the connection
    # and a tuple holding the address of the client.

    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)