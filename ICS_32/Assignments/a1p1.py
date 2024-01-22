from pathlib import Path
'''
myPath = Path(file_input)
        if myPath.exists():
            for folders in myPath.iterdir():
                print(folders)

#THIS IS -R
def recursive():
#THIS IS -F
def only_files():
    for paths in myPath.iterdir():
            if paths.isfile():
                 print(paths)
            
#THIS IS -S
def only_same_name():
#THIS IS -E
def only_same_extension():
'''
def content_list():
    for paths in myPath.iterdir():
        print(paths)


if __name__ == "__main__":
    user_input = "L /Users/justinle/VS_Code/ICS_32"

    while user_input != "Q":
        user_input_list = user_input.split()
        command = user_input_list[0]
        path = user_input_list[1]
        myPath = Path(path)
        if command != "L":
            print("Command can only be Q or L, Please choose again!")
            user_input = input()
        else:
            if myPath.exists():
                if len(user_input_list) == 2:
                    content_list()
                    user_input = input()
            else:
                 print("file or folder doesn't exist, Please choose again!")
                 user_input = input()
            