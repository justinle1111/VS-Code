# Starter code for assignment 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Justin Le
# lej42@uci.edu
# 50644854
import socket
import ds_protocol

server = "168.235.86.101"
port = 3021
def send(server:str, port:int, username:str, password:str, message:str, bio:str=None):
  '''
  The send function joins a ds server and sends a message, bio, or both

  :param server: The ip address for the ICS 32 DS server.
  :param port: The port where the ICS 32 DS server is accepting connections.
  :param username: The user name to be assigned to the message.
  :param password: The password associated with the username.
  :param message: The message to be sent to the server.
  :param bio: Optional, a bio for the user.
  '''
  #TODO: return either True or False depending on results of required operation
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((server, port))
    send = client.makefile('w') 
    recv = client.makefile('r')
    join_msg = ds_protocol.join(username, password)
    send.write(join_msg + '\r\n')
    send.flush()
    resp = recv.readline()
    resp = ds_protocol.extract_json(resp)
    token = resp.token
    if resp.type == "ok":
      msg = ds_protocol.post(token, message)
      client.sendall(msg.encode("utf-8"))
      if bio != "None":
        updated_bio = ds_protocol.bio(token, bio)
        client.sendall(updated_bio.encode("utf-8"))



    

