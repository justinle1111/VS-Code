import ds_messenger

server = "168.235.86.101"
port = 3021

username = "ILOVEKIMCHAEWON534912"
password = "AMONGUSPASSWORDSECRET"

direct_message = ds_messenger.DirectMessenger(server, username, password)
print(direct_message.retrieve_new())
print(direct_message.retrieve_all())