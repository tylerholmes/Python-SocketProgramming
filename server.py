import socket

def main():

    # Setup socket connection    
    host = "localhost"
    port = 8080
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host,port))
    sock.listen()
    conn,addr = sock.accept()

    # Keep server running and listening for client messages
    while True:
        message = conn.recv(1024)
        
        # Decode message bytes to string
        decoded_message = message.decode('utf-8')
        
        # Reverse messaage from client and encode
        response = decoded_message[::-1].encode('utf-8')
        conn.sendall(response)

        # Close connections if client sends "end" message
        if decoded_message == "end":
            conn.close()
            sock.close()
            return False
        
if __name__=="__main__":
    main()
