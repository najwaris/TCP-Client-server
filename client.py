import socket


def client_program():
    # both client and server run on the same machine
    host = socket.gethostname() 
    # port number for connection between server and client
    port = 5001 

    # establish connection
    client_socket = socket.socket() 
    # connect to server
    client_socket.connect((host, port)) 

    # receive the input 
    message = input(" -> ")  

    while message.lower().strip() != 'bye':
        # send the message to the server
        client_socket.send(message.encode()) 
        # receive response from server
        data = client_socket.recv(1024).decode() 

        # the response show in the terminal 
        print('Received from server: ' + data)  

        # again take input
        message = input(" -> ")  

    # close the connection 
    client_socket.close() 


if __name__ == '__main__':
    client_program()
