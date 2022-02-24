import socket

def main():
    host = "localhost"
    port = 5000
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    while True:
        message = input("Enter message: ")
        encoded_message = message.encode('utf-8')
        sock.sendall(encoded_message)
        echo = sock.recv(1024)
        decoded_echo = echo.decode('utf-8')
        print(f'Reverse echo from server: {decoded_echo}')
        if decoded_echo == "dne":
            sock.close()
            return False

if __name__=="__main__":
    main()