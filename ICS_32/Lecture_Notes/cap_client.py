import socket


def main ():

    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    my_socket.connect((socket.gethostname(), 6060))

    
    message = input ("Enter a string to be capitalized: ")

    print(f"Sending message to server: {message}")
    my_socket.send(message.encode('utf-8'))

    capitalized_message = my_socket.recv(2048).decode('utf-8')
    print(f"Received capitalized message from server: {capitalized_message}")

    
    my_socket.close()




if __name__ == "__main__":
    main()