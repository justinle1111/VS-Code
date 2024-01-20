#lab3.py
# Starter code for lab 3 in ICS 32 Programming with Software Libraries in Python
# Replace the following placeholders with your information.
# Please see the README in this repository for the requirements of this lab exercise
# Justin Le
# lej42@uci.edu
# 50644854
from pathlib import Path

def createFile():
    myPath = Path("/Users/justinle/VS Code /ICS 32 /Labs/pynote.txt")
    if myPath.exists():
        with open('pynote.txt', 'r') as myfile:
            print(myfile.read())
    else:
        with open('pynote.txt', 'x') as myfile:
            myfile.write("")

def welcomenote():
    print("Welcome to PyNote!")

def writeFile(user_input):
    with open('pynote.txt', 'a') as myfile:
            myfile.write(user_input + "\n")

if __name__ == "__main__":
    welcomenote()
    createFile()
    user_input = input("Please enter a new note (enter q to exit): ")
    while user_input != "q":
         writeFile(user_input)
         user_input = input("Please enter a new note (enter q to exit): ")
