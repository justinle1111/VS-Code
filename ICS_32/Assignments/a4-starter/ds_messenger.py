import socket
import ds_protocol
import json
server = "168.235.86.101"
port = 3021

class DirectMessage:
  def __init__(self):
    self.recipient = None
    self.message = None
    self.timestamp = None


class DirectMessenger:
  def __init__(self, dsuserver=None, username=None, password=None):
    self.token = None
    self.dsuserver = dsuserver
    self.username = username
    self.password = password
		
  def send(self, message:str, recipient:str) -> bool:
    # must return true if message successfully sent, false if send failed.
   with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    try:
      client.connect((server, port))
      send = client.makefile('w') 
      recv = client.makefile('r')
      join_msg = ds_protocol.join(self.username, self.password)
      send.write(join_msg + '\r\n')
      send.flush()
      resp = recv.readline()
      resp = ds_protocol.extract_json(resp)
      token = resp.token

      if resp.type == "ok":
        msg = ds_protocol.send_message(token, message, recipient)
        client.sendall(msg.encode("utf-8"))
        print("Message has been successfully sent (messenger send function)")
      return True
    except Exception as error:
      print("(Messenger.py)Send Error: ", error)
      return False

		
  def retrieve_new(self) -> list:
    # must return a list of DirectMessage objects containing all new messages
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
      client.connect((self.dsuserver, port))
      send = client.makefile('w') 
      recv = client.makefile('r')
      join_msg = ds_protocol.join(self.username, self.password)
      send.write(join_msg + '\r\n')
      send.flush()
      resp = recv.readline()
      resp = ds_protocol.extract_json(resp)
      token = resp.token

      if resp.type == "ok":
        msg = ds_protocol.direct_message_new(token)
        client.sendall(msg.encode("utf-8"))
        server_response = client.recv(4096)
        server_response = json.loads(server_response.decode("utf-8"))
        return server_response["response"]["messages"]

  def retrieve_all(self) -> list:
    # must return a list of DirectMessage objects containing all messages
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
      client.connect((self.dsuserver, port))
      send = client.makefile('w') 
      recv = client.makefile('r')
      join_msg = ds_protocol.join(self.username, self.password)
      send.write(join_msg + '\r\n')
      send.flush()
      resp = recv.readline()
      resp = ds_protocol.extract_json(resp)
      token = resp.token

      if resp.type == "ok":
        msg = ds_protocol.direct_message_all(token)
        client.sendall(msg.encode("utf-8"))
        server_response = client.recv(4096)
        server_response = json.loads(server_response.decode("utf-8"))
        return server_response["response"]["messages"]