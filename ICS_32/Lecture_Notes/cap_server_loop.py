import socket


def capitalize_text(text):
    return text.upper()

def main():
    
    port = 6060

    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.bind ((socket.gethostname(), 6060))
    my_socket.listen (5)
    print(f"Server listening on {socket.gethostname()}:{port}...")

    while True:
        client_socket, address = my_socket.accept()
        print (f"Connected to client {address}")

        while True:
            client_data = client_socket.recv(2048).decode('utf-8').strip()

            #The if not client_data: statement checks if the received data is empty or
            #if the client has closed the connection. If client_data is empty (i.e., an empty string), 
            #it means the client has closed the connection or no more data is being sent. In this case, 
            #the server breaks out of the loop and closes the connection with that client, 
            #moving on to accept new connections.
            if not client_data:
                break

            print(f"Received data from client: {client_data}")

            capitalized_text = capitalize_text(client_data)

            client_socket.send(capitalized_text.encode('utf-8'))
       
        client_socket.close()

if __name__ == "__main__":
    main()