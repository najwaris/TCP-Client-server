import socket


def server_program():

    # get the hostname
    host = socket.gethostname()
    # port same with the client for the connection 
    port = 5001  

    # establish connection with the client 
    server_socket = socket.socket() 
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        dataconn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        print("from connected user: " + str(data))
        data = input(' -> ')
        conn.send(data.encode())  # send data to the client

    # close the connection
    conn.close()  


if __name__ == '__main__':
    server_program()