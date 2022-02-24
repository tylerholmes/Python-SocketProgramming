import socket

def main():
    host = "localhost"
    port = 5000
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host,port))
    sock.listen()
    conn,addr = sock.accept()
    while True:
        message = conn.recv(1024)
        decoded_message = message.decode('utf-8')
        response = decoded_message[::-1].encode('utf-8')
        conn.sendall(response)
        if decoded_message == "end":
            conn.close()
            sock.close()
            return False
        
if __name__=="__main__":
    main()