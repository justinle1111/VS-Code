import shlex
user_input = "E -usr \"mark b\" -pwd \"password123\""
user_input = user_input.split("-")
user_input = user_input[1:]
for options in user_input:
    pass