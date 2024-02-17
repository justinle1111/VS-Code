#lab12.py
#
# Starter code for lab 12 in ICS 32
# Programming with Software Libraries in Python
#
# Replace the following placeholders with your information.
# Please see the Canvas assignment prompt for the requirements
# of this lab exercise

# Justin Le
# lej42
# 50644854

import json
import time
import random


def to_json(obj: dict) -> str:
    """
    serializes a python dictionary object to a json formatted string
    returns None if object cannot be serialized to json
    """
    try:
        data = json.dumps(obj)
        return data
    except:
        return None


def from_json(obj: str) -> any:
    """
    deserializes a json formatted string to a python type.
    return type depends on json structure.
    returns None if string cannot be deserialized from json
    """
    try:
        data = json.loads(obj)
        return data
    except:
        return None

def run_test() -> None:
    time_created = time.ctime()
    random_number = random.randint(1, 5)
    visited_random = []
    for i in range(random_number):
        visited_random.append(time.time())
    my_json_format = {"url": "https://www.ics.uci.edu", "time_create": time_created, "visited": [visited_random]}
    """
    You will have to decide how you will create your format for testing.
    The simplest approach might
    the following (note this example is missing some requirements on purpose):

    my_json_format = {"url": "https://www.ics.uci.edu"}

    A better approach would be to write a function that will accept the
    required data as parameter(s)
    and return a value that is in the format you have designed.

    You might also consider generating multiple test conditions.
    If you would like to place the print test code
    below into a loop to print multiple conditions, feel free to change it.
    """
    j = to_json(my_json_format)

    print(j)

    if j is not None:
        d = from_json(j)
        print(d)
    else:
        print("Unable to deserialize object")

if __name__ == "__main__":
    run_test()
