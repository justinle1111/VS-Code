from pathlib import Path
#lab4.py
# Starter code for lab 4 in ICS 32 Programming with Software Libraries in Python
# Replace the following placeholders with your information.
# Please see the README in this repository for the requirements of this lab exercise
# Justin Le
# lej42
# 50644854

#THIS IS -R
def recursive(path):
    for paths in path.iterdir():
        if paths.is_dir():
            print(paths)
            recursive(paths)
        else:
            print(paths)

#Command R
def read_contents(path, myPath):
    if myPath.exists():
        if "dsu" in path:
            with open(myPath) as f:
                file = f.read()
                print(file)
        else:
            print("Error")

#Command D
def delete_file(path, myPath):
    if myPath.exists():
        if "dsu" in path:
            myPath.unlink()
            print(path, "DELETED")
    else:
        print("Error")
#THIS IS -F
def only_files(path):
    for paths in path.iterdir():
        if paths.is_file():
            print(paths)
  
#THIS IS -S
def only_same_name(path, keyword):
    for paths in path.iterdir():
        path_string = str(paths)
        path_name = path_string.split("/")
        if path_name[-1] == keyword:
            print(paths)
#THIS IS -E
def only_same_extension(path, keyword):
    for paths in path.iterdir():
        path_string = str(paths)
        path_name = path_string.split("/")
        if keyword in path_name[-1]:
            print(paths)

#This is R and F
def recursive_files(path):
    for paths in path.iterdir():
        if paths.is_dir():
            recursive_files(paths)
        else:
            print(paths)

#This is R and E
def recursive_extension(path, keyword):
    for paths in path.iterdir():
        path_string = str(paths)
        path_name = path_string.split("/")
        if paths.is_dir():
            recursive_extension(paths, keyword)
        else:
            if keyword in path_name[-1]:
                print(paths)

#R and S
def recursive_name(path, keyword):
    for paths in path.iterdir():
        path_string = str(paths)
        path_name = path_string.split("/")
        if paths.is_dir():
            recursive_name(paths, keyword)
        else:
            if path_name[-1] == keyword:
                print(paths)

def content_list():
    for paths in myPath.iterdir():
        print(paths)


if __name__ == "__main__":
    user_input = input()
    while user_input != "Q":
        user_input_list = user_input.split()
        command = user_input_list[0]
        try:
            path = user_input_list[1]
            myPath = Path(path)
        except:
            path = ""
        if command == "L":
            if myPath.exists():
                if len(user_input_list) == 2:
                        content_list()
                        user_input = input()
                elif len(user_input_list) == 3:
                    option = user_input_list[2]
                    if option == "-r":
                        recursive(myPath)
                        user_input = input()
                    elif option == "-f":
                        only_files(myPath)
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
                        only_same_extension(myPath, other_input)
                        user_input = input()
                    elif option == "-s":
                        only_same_name(myPath, other_input)
                        user_input = input()
                    elif option == "-r" and other_input == "-f":
                        recursive_files(myPath)
                        user_input = input()
                elif len(user_input_list) == 5:
                    option = user_input_list[2]
                    other_input = user_input_list[3]
                    another_input = user_input_list[4]
                    if option == "-r" and other_input == "-e":
                        recursive_extension(myPath, another_input)
                        user_input = input()
                    elif option == "-r" and other_input == "-s":
                        recursive_name(myPath, another_input)
                        user_input = input()
            else:
                 print("file or folder doesn't exist, Please choose again!")
                 user_input = input()
        elif command == "D":
            if myPath.exists():
                delete_file(path, myPath)
                user_input = input()
            else:
                print("file or folder doesn't exist, Please choose again!")
                user_input = input()
        elif command == "R":
            if myPath.exists():
                read_contents(path, myPath)
                user_input = input()
        elif command == "C":
            try:
                option = user_input_list[2]
                file_name = user_input_list[3]
                if myPath.exists():
                    if option == "-n":
                        create_file(myPath, file_name)
                        user_input = input()
                    else:
                        print("Error")
                        user_input = input()
            except:
                print("Error")
                user_input = input()
        else:
            print("Invalid Command")
            user_input = input()

def create_file(path, file_name):
    file_name = file_name + ".dsu"
    file_path = path / file_name
    file_path.touch()
    return file_path

def command_C(path, user_input):
    try:
        input_1 = initial_user_input_list[2]
        name = initial_user_input_list[3]
    except:
        print("Invalid Format, Must Use [C] [input] [[-]option] [name]")
    test_file = path + "/" + name + ".dsu"
    test_path = Path(test_file)
    if test_path.exists():
        print("File exists will Load")
        command_O(test_file)
    else:
        newPath = Path(path)
        newFile = create_file(newPath, name)
        new_user_username = input("Please enter a username: ")
        new_user_password = input("Please enter a password: ")
        new_user_profile = Profile(dsuserver=str(newFile), username=new_user_username, password=new_user_password)
        new_user_profile.save_profile(newFile)
        command_O(test_file)

def command_O(path):
    if ".dsu" in path:
        user_profile = Profile()
        user_profile.load_profile(path)
        print("Profile has been loaded")
    else:
        print("path is not a dsu file")

def command_P(path, user_input_list):
    try:
        action = user_input_list[1]
    except:
        print("Invalid Input")
    profile = Profile()
    profile.load_profile(path)
    if len(user_input_list) == 2:
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
    elif len(user_input_list) == 3:
        pass
    elif len(user_input_list) == 4:
        pass
    else:
        print("Either you put more than 2 options or invalid options, please ")
def command_E(path, user_input_list):
    try:
        action = user_input_list[1]
        option = user_input_list[2]
    except:
        print("Invalid Action or Option")
    profile = Profile()
    profile.load_profile(path)
    if action == "-usr":
        profile = Profile(username=option)
        profile.save_profile(path)
    elif action == "-pwd":
        profile = Profile(password=option)
        profile.save_profile(path)
    elif action == "-bio":
        profile = Profile(bio=option)
        profile.save_profile(path)
    elif action == "-addpost":
        post = Post()
        post.set_entry(option)
        profile = Profile()
        profile.load_profile(path)
        profile.get_posts()
        profile.add_post(post)
        profile.save_profile(path)
    elif action == "-delpost":
        try:
            option = int(option)
        except:
            print("option is not a number")
        profile = Profile()
        profile.load_profile(path)
        profile.get_posts()
        profile.del_post(option)
        profile.save_profile(path)
    else:
        print("Invalid Input")
