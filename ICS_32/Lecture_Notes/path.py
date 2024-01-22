from pathlib import Path

def print_paths(path_name):
    myPath = Path(path_name)
    for currentPath in myPath.iterdir():
        if(currentPath.is_dir()):
            print_paths(currentPath)
        print(currentPath)

if __name__ == "__main__":
    print_paths("/Users/justinle/VSCode/ICS32/a0.py")