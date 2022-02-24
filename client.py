import socket

def main():
    # Setup socket connection
    host = "localhost"
    port = 8080
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    
    # Keep client running until "dne" is received from server
    while True:
        message = input("Enter message: ")
        
        # Encode string to bytes using utf-8 to send over socket connection
        encoded_message = message.encode('utf-8')
        sock.sendall(encoded_message)
        
        # Receive and decode message from server
        echo = sock.recv(1024)
        decoded_echo = echo.decode('utf-8')
        print(f'Reverse echo from server: {decoded_echo}')
        
        # Connection is closed once if the response from server is the reverse of "end"
        if decoded_echo == "dne":
            sock.close()
            return False

if __name__=="__main__":
    main()
