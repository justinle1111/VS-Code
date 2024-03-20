import ds_protocol
import ds_client_a4

server = "168.235.86.101"
port = 3021
token = "user_token"
entry = "Hello World!"
recipient = "ohhimark"
username = "ILOVEKIMCHAEWON534912"
password = "AMONGUSPASSWORDSECRET"
recipient = "saitama"

response = ds_client_a4.send(server, port, username, password, "I like turtles", recipient)

print(response)