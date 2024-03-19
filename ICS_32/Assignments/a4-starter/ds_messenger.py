import socket
import ds_protocol
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
          msg = ds_protocol.request_direct_message(token, "new")
          client.sendall(msg.encode("utf-8"))
          print("Retrieve New Works")
        return msg
      except Exception as error:
        print("(Messenger.py) Retrieve_new Error: ", error)
        return False
 
  def retrieve_all(self) -> list:
    # must return a list of DirectMessage objects containing all messages
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
      try:
        client.connect((server, port))
        send = client.makefile('w') 
        recv = client.makefile('r')
        join_msg = ds_protocol.join()
        send.write(join_msg + '\r\n')
        send.flush()
        resp = recv.readline()
        resp = ds_protocol.extract_json(resp)
        token = resp.token

        if resp.type == "ok":
          msg = ds_protocol.request_direct_message(token, "all")
          client.sendall(msg.encode("utf-8"))
          print("Retrieve All Works")
        return msg
      except Exception as error:
        print("(Messenger.py) Retrieve_all Error: ", error)
        return False