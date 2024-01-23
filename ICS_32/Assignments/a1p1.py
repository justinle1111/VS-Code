from pathlib import Path

#THIS IS -R
def recursive(path):
    for paths in path.iterdir():
        if paths.is_dir():
            print(paths)
            recursive(paths)
        else:
            print(paths)

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
        elif command != "L" or command != "Q":
            print("command must be L or Q, try again")
            user_input = input()