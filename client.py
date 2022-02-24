import socket

def main():
    host = "localhost"
    port = 5000
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    while True:
        message = input("Enter message")
        sock.sendall(message)
        echo = sock.recv(1024)
        print("Rever echo: {echo}")
        if echo == "dne":
            return False

