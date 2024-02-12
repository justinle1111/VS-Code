# a2.py

# Starter code for assignment 2 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Justin Le
# lej42
# 50644854
from pathlib import Path
from Profile import Profile
import shlex 
def create_file(path, file_name):
    file_name = file_name + ".dsu"
    file_path = path / file_name
    file_path.touch()
    return file_path

def command_C(path, user_input):
    try:
        input_1 = user_input_list[2]
        name = user_input_list[3]
        newPath = Path(path)
        create_file(newPath, name)
    except:
        print("Invalid Format, Must Use [C] [input] [[-]option] [name]")
    new_user_username = input("Please enter a username: ")
    new_user_password = input("Please enter a password: ")
    new_user_profile = Profile(dsuserver=str(create_file(newPath, name)), username=new_user_username, password=new_user_password)
    new_user_profile.save_profile(create_file(newPath, name))
    return str(newPath)
def command_O(path, user_input):
    try:
        if ".dsu" in path:
            newPath = Path(path)
            user_profile = Profile()
            user_profile.load_profile(newPath)
            print("Profile has been loaded")
        else:
            print("file is not a dsu file")
        return str(newPath)
    except:
        print("Error: Path doesn't exist")
        newPath = ""
        return newPath
def command_P(path, user_input_list):
    try:
        action = user_input_list[1]
    except:
        print("Invalid Input")
    profile = Profile()
    profile.load_profile(path)

    if action == "-usr":
        print(profile.username)
    elif action == "-pwd":
        print(profile.password)
    elif action == "-bio":
        print(profile.bio)
    elif action == "-posts":
        print(profile._posts)
    elif action == "-post":
        try:
            id = user_input_list[2]
            print(profile._posts[id])
        except:
            print("Id of post is invalid")
    elif action == "-all":
        print(profile.username, profile.password, profile.bio, profile._posts)
    else:
        print("Invalid option")

if __name__ == "__main__":
    user_input = input()
    user_input_list = shlex.split(user_input)
    try:
        path = user_input_list[1]
    except:
        path = ""
    while user_input != "Q":
        if user_input[0] == "C":
            command_C(path, user_input)
        elif user_input[0] == "O":
            command_O(path, user_input)
        elif user_input[0] == "P":
            command_P(path, user_input_list)
        elif user_input[0] == "E":
            pass
        user_input = input()



                                           