# a2.py

# Starter code for assignment 2 in ICS 32 Programming with Software Libraries in Python
# Replace the following placeholders with your information.

# Justin Le
# lej42
# 50644854
from pathlib import Path
from Profile import Profile
from Profile import Post
import ui
import shlex 

if __name__ == "__main__":
    user_input = input()
    initial_user_input_list = shlex.split(user_input)
    if user_input == "admin":
        user_input = input()
    try:
        path = initial_user_input_list[1]
    except:
        pass
    while user_input != "Q":
        if user_input[0] == "C":
            user_input_list = shlex.split(user_input)
            if len(user_input_list) == 4:
                try: 
                    option = user_input_list[2]
                except:
                    print("Invalid command")
                if option == "-n":
                    name = user_input_list[3]
                    newPath = ui.command_C(path, name)
                    ui.command_O(newPath)
                else:
                    print("Invalid Option, must be -n")
            else:
                print("Invalid Command, not length of 4")
        elif user_input[0] == "O":
            user_input_list = shlex.split(user_input)
            if len(user_input_list) == 2:
                path = user_input_list[1]
                ui.command_O(path)
            else:
                print("Invalid Command, not length of 2")
        elif user_input[0] == "P":

            user_input_list = shlex.split(user_input)
            if initial_user_input_list[0] == "C":
                newPath = initial_user_input_list[1] + "/" + initial_user_input_list[3] + ".dsu"
            else:
                newPath = initial_user_input_list[1]
            ui.command_P(newPath, user_input_list)
        elif user_input[0] == "E":
            user_input_list = shlex.split(user_input)
            if initial_user_input_list[0] == "C":
                newPath = initial_user_input_list[1] + "/" + initial_user_input_list[3] + ".dsu"
            else:
                newPath = initial_user_input_list[1]
            ui.command_E(newPath, user_input_list)
        elif user_input[0] == "R":
            user_input_list = shlex.split(user_input)
            if len(user_input_list) == 2:
                try:
                    path = user_input_list[1]
                    myPath = Path(path)
                except:
                    print("path doesn't exist")
                if myPath.exists():
                    ui.read_contents(path, myPath)
                else:
                    print("file or folder doesn't exist, Please choose again!")
            else:
                print("Invalid Command")
        elif user_input[0] == "L":
            myPath = Path(path)
            if myPath.exists():
                if len(user_input_list) == 2:
                        ui.content_list()
                        user_input = input()
                elif len(user_input_list) == 3:
                    option = user_input_list[2]
                    if option == "-r":
                        ui.recursive(myPath)
                        user_input = input()
                    elif option == "-f":
                        ui.only_files(myPath)
                        user_input = input()
                    elif option == "-e":
                        print("Need to specify file name, try again!")
                        user_input = input()
                    elif option == "-s":
                        print("Need to specify file extension, try again!")
                        user_input = input()
                    else: 
                        print("Invalid Option must be -r, -f, -e, or -s, Try again!")
                        user_input = input()
                elif len(user_input_list) == 4:
                    option = user_input_list[2]
                    other_input = user_input_list[3]
                    if option == "-e":
                        ui.only_same_extension(myPath, other_input)
                        user_input = input()
                    elif option == "-s":
                        ui.only_same_name(myPath, other_input)
                        user_input = input()
                    elif option == "-r" and other_input == "-f":
                        ui.recursive_files(myPath)
                        user_input = input()
                elif len(user_input_list) == 5:
                    option = user_input_list[2]
                    other_input = user_input_list[3]
                    another_input = user_input_list[4]
                    if option == "-r" and other_input == "-e":
                        ui.recursive_extension(myPath, another_input)
                        user_input = input()
                    elif option == "-r" and other_input == "-s":
                        ui.recursive_name(myPath, another_input)
                        user_input = input()
            else:
                print("file or folder doesn't exist, Please choose again!")
                user_input = input()
        elif user_input[0] == "D":
            user_input_list = shlex.split(user_input)
            if len(user_input_list) == 2:
                try:
                    path = user_input_list[1]
                    myPath = Path(path)
                except:
                    print("path doesn't exist")
                if myPath.exists():
                    ui.delete_file(path, myPath)
                else:
                    print("file or folder doesn't exist, Please choose again!")
            else:
                print("Invalid Command")
        user_input = input()
