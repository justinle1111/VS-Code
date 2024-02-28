# ui.py

# Starter code for assignment 2 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Justin le
# lej42
# 50644854
from pathlib import Path
from Profile import Profile
from Profile import Post
import ds_client
server = "168.235.86.101"
port = 3021
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

#Command C
def create_file(path, file_name):
    newPath = Path(path)
    file_name = file_name + ".dsu"
    file_path = newPath / file_name
    file_path.touch()
    print(file_path)

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

def content_list(myPath):
    for paths in myPath.iterdir():
        print(paths)

def create_file(path, file_name):
    file_name = file_name + ".dsu"
    file_path = path / file_name
    file_path.touch()
    return file_path

def command_C(path, name):
    
    test_file = path + "/" + name + ".dsu"
    test_path = Path(test_file)
    if test_path.exists():
        print("File exists will Load")
        return(str(test_path))
    else:
        newPath = Path(path)
        newFile = create_file(newPath, name)
        new_user_username = input("Please enter a username: ")
        new_user_password = input("Please enter a password: ")
        new_user_profile = Profile(dsuserver=str(newFile), username=new_user_username, password=new_user_password)
        new_user_profile.save_profile(newFile)
        new_user_profile.load_profile(newFile)
        return(str(newFile))

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
        elif action == "-all":
            print(profile.username, profile.password, profile.bio, profile._posts)
    elif len(user_input_list) == 3:

        additional_option = user_input_list[2]
        if action == "-post":
            try:
                id = user_input_list[2]
                print(profile._posts[id])
            except:
                print("Id of post is invalid")
        elif action == "-usr" and additional_option == "-pwd":
            print(profile.username, profile.password)
        elif action == "-usr" and additional_option == "-bio":
            print(profile.username, profile.bio)
        elif action == "-usr" and additional_option == "-posts":
            print(profile.username, profile._posts)
        elif action == "-pwd" and additional_option == "-usr":
            print(profile.username, profile.password)
        elif action == "-pwd" and additional_option == "-bio":
            print(profile.bio, profile.password)
        elif action == "-pwd" and additional_option == "-posts":
            print(profile._posts, profile.password)
        elif action == "-bio" and additional_option == "-usr":
            print(profile.username, profile.bio)
        elif action == "-bio" and additional_option == "-pwd":
            print(profile.password, profile.bio)
        elif action == "-bio" and additional_option == "-posts":
            print(profile._posts, profile.bio)
        else:
            print("Invalid Input")
    elif len(user_input_list) == 4 and action == "-post":
        additional_option_post = user_input_list[3]
        if action == "-post" and additional_option_post == "-usr":
            try:
                id = user_input_list[2]
                print(profile._posts[id], profile.username)
            except:
                print("Id of post is invalid")
        elif action == "-post" and additional_option_post == "-pwd":
            try:
                id = user_input_list[2]
                print(profile._posts[id], profile.password)
            except:
                print("Id of post is invalid")
        elif action == "-post" and additional_option_post == "-bio":
            try:
                id = user_input_list[2]
                print(profile._posts[id], profile.bio)
            except:
                print("Id of post is invalid")
        else:
            print("Invalid option")
        if len(user_input_list) == 4 and action != "-post":
            additional_option = user_input_list[2]
            id = user_input_list[3]
            print(additional_option, id, action)
            if action == "-usr" and additional_option_post == "-post":
                try:
                    id = user_input_list[3]
                    print(profile.username, profile._posts[id])
                except:
                    print("Invalid ID")
            elif action == "-bio" and additional_option_post == "-post":
                try:
                    id = user_input_list[3]
                    print(profile.bio, profile._posts[id])
                except:
                    print("Invalid ID")
            elif action == "-pwd" and additional_option_post == "-post":
                try:
                    id = user_input_list[3]
                    print(profile.password, profile._posts[id])
                except:
                    print("Invalid ID")
            else:
                print("Invalid Input")
        else:
            print("invalid option")
    else:
        print("Invalid option")

def command_E(path, user_input_list):
    try:
        action = user_input_list[1]
        option = user_input_list[2]
    except:
        print("Invalid Action or Option")
    profile = Profile()
    profile.load_profile(path)
    if len(user_input_list) == 3:
        if action == "-usr":
            profile.username = option
            profile.save_profile(path)
        elif action == "-pwd":
            profile.password = option
            profile.save_profile(path)
        elif action == "-bio":
            profile.bio = option
            profile.save_profile(path)
        elif action == "-addpost":
            post = Post()
            post.set_entry(option)
            profile = Profile()
            profile.load_profile(path)
            profile.get_posts()
            profile.add_post(post)
            profile.save_profile(path)
            ds_client.send(server, port, profile.username, profile.password, option, profile.bio)
            print("Uploaded to server")
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
            print("Invalid, Len 3")
    elif len(user_input_list) == 5:
        action_2 = user_input_list[3]
        option_2 = user_input_list[4]
        if action == "-usr" and action_2 == "-pwd":
            profile.username = option
            profile.password = option_2
            profile.save_profile(path)
        elif action == "-usr" and action_2 == "-bio":
            profile.username = option
            profile.bio = option_2
            profile.save_profile(path)
        elif action == "-usr" and action_2 == "-addpost":
            profile.username = option
            post = Post()
            post.set_entry(option_2)
            profile = Profile()
            profile.load_profile(path)
            profile.get_posts()
            profile.add_post(post)
            profile.save_profile(path)
            ds_client.send(server, port, profile.username, profile.password, option_2, profile.bio)
            print("Uploaded to server")
        elif action == "-usr" and action_2 == "-delpost":
            profile.username = option
            post = Post()
            post.set_entry(option_2)
            profile = Profile()
            profile.load_profile(path)
            profile.get_posts()
            profile.del_post(post)
            profile.save_profile(path)
        elif action == "-pwd" and action_2 == "-usr":
            profile.password = option
            profile.username = option_2
            profile.save_profile(path)
        elif action == "-pwd" and action_2 == "-bio":
            profile.password = option
            profile.bio = option_2
            profile.save_profile(path)
        elif action == "-pwd" and action_2 == "-addpost":
            profile.password = option
            post = Post()
            post.set_entry(option_2)
            profile = Profile()
            profile.load_profile(path)
            profile.get_posts()
            profile.add_post(post)
            profile.save_profile(path)
            ds_client.send(server, port, profile.username, profile.password, option_2, profile.bio)
            print("Uploaded to server")
        elif action == "-pwd" and action_2 == "-delpost":
            profile.password = option
            post = Post()
            post.set_entry(option_2)
            profile = Profile()
            profile.load_profile(path)
            profile.get_posts()
            profile.del_post(post)
            profile.save_profile(path)

        elif action == "-addpost" and action_2 == "-usr":
            post = Post()
            post.set_entry(option)
            profile = Profile()
            profile.load_profile(path)
            profile.get_posts()
            profile.add_post(post)
            profile.username = option_2
            profile.save_profile(path)
            ds_client.send(server, port, profile.username, profile.password, option, profile.bio)
            print("Uploaded to server")
        elif action == "-addpost" and action_2 == "-bio":
            post = Post()
            post.set_entry(option)
            profile = Profile()
            profile.load_profile(path)
            profile.get_posts()
            profile.add_post(post)
            profile.bio = option_2
            profile.save_profile(path)
        elif action == "-addpost" and action_2 == "-password":
            post = Post()
            post.set_entry(option)
            profile = Profile()
            profile.load_profile(path)
            profile.get_posts()
            profile.add_post(post)
            profile.password = option_2
            profile.save_profile(path)
            ds_client.send(server, port, profile.username, profile.password, option, profile.bio)
            print("Uploaded to server")
        elif action == "-addpost" and action_2 == "-delpost":
            post = Post()
            post.set_entry(option)
            profile = Profile()
            profile.load_profile(path)
            profile.get_posts()
            profile.add_post(post)
            profile.password = option_2
            profile.save_profile(path)
            post = Post()
            post.set_entry(option_2)
            profile = Profile()
            profile.load_profile(path)
            profile.get_posts()
            profile.del_post(post)
            profile.save_profile(path)
            ds_client.send(server, port, profile.username, profile.password, option, profile.bio)
            print("Uploaded to server")
        elif action == "-delpost" and action_2 == "-usr":
            post = Post()
            post.set_entry(option)
            profile = Profile()
            profile.load_profile(path)
            profile.get_posts()
            profile.del_post(post)
            profile.username = option_2
            profile.save_profile(path)
        elif action == "-delpost" and action_2 == "-bio":
            post = Post()
            post.set_entry(option)
            profile = Profile()
            profile.load_profile(path)
            profile.get_posts()
            profile.del_post(post)
            profile.bio = option_2
            profile.save_profile(path)
        elif action == "-delpost" and action_2 == "-password":
            post = Post()
            post.set_entry(option)
            profile = Profile()
            profile.load_profile(path)
            profile.get_posts()
            profile.del_post(post)
            profile.password = option_2
            profile.save_profile(path)
        elif action == "-delpost" and action_2 == "-addpost":
            post = Post()
            post.set_entry(option)
            profile = Profile()
            profile.load_profile(path)
            profile.get_posts()
            profile.del_post(post)
            post = Post()
            post.set_entry(option_2)
            profile = Profile()
            profile.load_profile(path)
            profile.get_posts()
            profile.add_post(post)
            profile.save_profile(path)
            ds_client.send(server, port, profile.username, profile.password, option_2, profile.bio)
            print("Uploaded to server")
        else:
            print("Invalid, Len 4")
    else:
        print("Invalid Input Please only put 2 actions")


