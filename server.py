import socket

def main():
    host = "localhost"
    port = 5000
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host,port))
    while True:
        sock.listen()
        conn,addr = sock.accept()
        message = conn.recv(1024)
        if message == "end":
            conn.sendall("dne")
            conn.close()
            return False
        else:
            conn.sendall(message[::-1])
        
