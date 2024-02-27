# ds_protocol.py

# Starter code for assignment 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

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
