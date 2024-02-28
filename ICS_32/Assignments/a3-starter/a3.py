# a3.py

# Starter code for assignment 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Justin Le
# lej42@uci.edu
# 50644854

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
    print("Welcome! Do you want to create or load a DSU file (type 'C' to create or 'O' to load)")
    user_input = input()
    if user_input == "admin":
        print("You are in Admin Mode")
        user_input = input()
        initial_user_input_list = shlex.split(user_input)
        
        while user_input != "Q":
            try:
                path = initial_user_input_list[1]
            except:
                print("Invalid user_input, Please try again")
                break
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
                if len(user_input_list) != 1:
                    if initial_user_input_list[0] == "C":
                        newPath = initial_user_input_list[1] + "/" + initial_user_input_list[3] + ".dsu"
                    else:
                        newPath = initial_user_input_list[1]
                    ui.command_P(newPath, user_input_list)
                else:
                    print("Invalid Command")
            elif user_input[0] == "E":
                user_input_list = shlex.split(user_input)
                if len(user_input_list) != 1:
                    if initial_user_input_list[0] == "C":
                        newPath = initial_user_input_list[1] + "/" + initial_user_input_list[3] + ".dsu"
                    else:
                        newPath = initial_user_input_list[1]
                    ui.command_E(newPath, user_input_list)
                else:
                    print("Invalid Command")
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
                            ui.content_list(myPath)
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
    elif user_input == "C":
        print("Great! What is the name of the file you would like to create?")
        C_input = input()
        print("Thank You, what path would u want that to be created?")
        path_C = input()
        try:
            path = Path(path_C)
            newPath = ui.command_C(path_C, C_input)
            ui.command_O(newPath)
            print("You have just created the file!!!")
            works = True
        except:
            print("Invalid path")
            works = False
        if works:
            print_list = []
            edit_list = []

            print("Do you want to Print or Edit the file (type 'P' to print or 'E' to edit or if you want to quit 'Q')")
            print_edit_input = input()
            print_list.append(print_edit_input)
            edit_list.append(print_edit_input)
            while print_edit_input != "Q":
                if print_edit_input == "P":
                    print("What do you want to print, Please choose from these options:")
                    print("username, password, bio, all posts, post, all")
                    print("Type '-usr' for username, '-pwd' for password, '-bio' for bio, '-posts' for all posts, '-post' for one post, or '-all' for all")
                    p_input = input()
                    print_list.append(p_input)
                    if print_list[1] == "-post":
                        print("Please put the ID of the post:")
                        post_id = input()
                        print_list.append(post_id)
                        ui.command_P(newPath, print_list)
                    else:
                        ui.command_P(newPath, print_list)
                    print_list = ['P']
                elif print_edit_input == "E":
                    print("What do you want to edit, Please choose from these options:")
                    print("username, password, bio, add post, delete post")
                    print("Type '-usr' for username, '-pwd' for password, '-bio' for bio, '-addpost' for add post, '-delpost' for delete post")
                    e_input = input()
                    edit_list.append(e_input)
                    print("Add the item you want to change")
                    print("For username type what you want the username to be, for password type what you want the password to be, for bio type what you want the bio to be")
                    print("To add a post please put '[thing you want to post]', then to delete a post please put the id of the post you want to delete")
                    e_item_input = input()
                    edit_list.append(e_item_input)
                    ui.command_E(newPath, edit_list)
                    print("To see your change please use the print command")
                    print(edit_list)
                    edit_list = ['E']
                else:
                    print("Invalid Command Try Again")
                print_edit_input = input("Do you want to Print or Edit the file (type 'P' to print or 'E' to edit or if you want to quit 'Q'\n")
        else:
            quit()

    elif user_input == "O":
        print("Great! What is the name of the file you would like to load?")
        O_input = input()
        try:
            path = Path(O_input)
            if path.exists():
                ui.command_O(O_input)
            works = True
        except:
            print("File doesn't exist")
            works = False
        if works:
            print_list = []
            edit_list = []

            print("Do you want to Print or Edit the file (type 'P' to print or 'E' to edit or if you want to quit 'Q')")
            print_edit_input = input()
            print_list.append(print_edit_input)
            edit_list.append(print_edit_input)
            while print_edit_input != "Q":
                if print_edit_input == "P":
                    print("What do you want to print, Please choose from these options:")
                    print("username, password, bio, all posts, post, all")
                    print("Type '-usr' for username, '-pwd' for password, '-bio' for bio, '-posts' for all posts, '-post' for one post, or '-all' for all")
                    p_input = input()
                    print_list.append(p_input)
                    if print_list[1] == "-post":
                        print("Please put the ID of the post:")
                        post_id = input()
                        print_list.append(post_id)
                        ui.command_P(path, print_list)
                    else:
                        ui.command_P(path, print_list)
                    print_list = ['P']
                elif print_edit_input == "E":
                    print("What do you want to edit, Please choose from these options:")
                    print("username, password, bio, add post, delete post")
                    print("Type '-usr' for username, '-pwd' for password, '-bio' for bio, '-addpost' for add post, '-delpost' for delete post")
                    e_input = input()
                    edit_list.append(e_input)
                    print("Add the item you want to change")
                    print("For username type what you want the username to be, for password type what you want the password to be, for bio type what you want the bio to be")
                    print("To add a post please put '[thing you want to post]', then to delete a post please put the id of the post you want to delete")
                    e_item_input = input()
                    edit_list.append(e_item_input)
                    ui.command_E(path, edit_list)
                    print("To see your change please use the print command")
                    print(edit_list)
                    edit_list = ['E']
                else:
                    print("Invalid Command Try Again")
                print_edit_input = input("Do you want to Print or Edit the file (type 'P' to print or 'E' to edit or if you want to quit 'Q'\n")
        else:
            quit()
