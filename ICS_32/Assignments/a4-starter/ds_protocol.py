# ds_protocol.py

#Assignment 4

# Justin Le
# lej42@uci.edu
# 50644854

import json
from collections import namedtuple
import time
# Namedtuple to hold the values retrieved from json messages.
# TODO: update this named tuple to use DSP protocol keys
DataTuple = namedtuple('response', ['type', 'message', 'token'])

def extract_json(json_msg:str) -> DataTuple:
  '''
  Call the json.loads function on a json string and convert it to a DataTuple object
  '''
  try:
    json_obj = json.loads(json_msg)
    type = json_obj['response']['type']
    message = json_obj['response']['message']
    token = json_obj['response']['token']

  except json.JSONDecodeError:
    print("Json cannot be decoded.")

  return DataTuple(type, message, token)

def join(username, password):
  message = {"join": {"username": username,"password": password,"token":""}}
  return json.dumps(message)

def post(token, post):
  timestamp = time.time()
  message = {"token":token, "post": {"entry": post,"timestamp": timestamp}}
  return json.dumps(message)

def bio(token, bio):
  timestamp = time.time()
  message = {"token":token, "bio": {"entry": bio,"timestamp": timestamp}}
  return json.dumps(message)

def send_message(token, entry, recipient):
  timestamp = time.time()
  message = {"token":token, "direct_message": {"entry": entry, "recipient": recipient, "timestamp": timestamp}}
  return json.dumps(message)

def request_direct_message(token, direct_message):
  if direct_message == "new":
    message = {"token":token, "direct_message": direct_message}
    print("Requesting New")
  elif direct_message == "all":
    message = {"token":token, "direct_message": direct_message}
    print("Requesting All")
  else:
    print("Part 1 Direct Message Error")
  return json.dumps(message)


def json_to_list(json_string):
  try:
    converted_json_string = json.loads(json_string)
  except json.JSONDecodeError:
    print("Json can't be decoded")
  return converted_json_string
