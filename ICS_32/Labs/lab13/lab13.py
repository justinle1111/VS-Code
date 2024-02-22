#lab13.py
#
# Starter code for lab 13 in ICS 32
# Programming with Software Libraries in Python
#
# Replace the following placeholders with your information.
# Please see the README in this repository for the requirements of this lab exercise

# NAME
# EMAIL
# STUDENT ID

import urllib
import bookmark_connection as bmc
from bookmark_connection import BookmarkProtocol
from urllib.parse import urlparse
from urllib.parse import urlencode, urlparse, quote_plus

"""
The following code snippets can be used to help you prepare your test function:
The url to use for testing.
Be sure to run bookmark_server.py before making requests!

url = 'http://localhost:8000'

The format to use for your request data.
Don't forget to encode before sending a request!

json = {'data':bmc.BookmarkProtocol.format(
                                BookmarkProtocol(BookmarkProtocol.ADD, data))}
"""

def http_api_test(url):
    # TODO: write your http connection code here. You can use the above snippets to help
    parsed_url = urlparse(url)
    json = {'data':bmc.BookmarkProtocol.format(
                                BookmarkProtocol(BookmarkProtocol.ADD, url))}
    json_encoded = urlencode(json, quote_via=quote_plus)
    json_encoded = json_encoded.encode("utf-8")
    print(json_encoded)

if __name__ == '__main__':
    url = 'http://localhost:8000'
    # TODO: call your test code from here. You might try writing a few different url tests.
    http_api_test(url)

