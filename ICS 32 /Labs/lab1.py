# lab1.py
# Starter code for lab 1 in ICS 32 Programming with Software Libraries in Python
# Replace the following placeholders with your information.
# Please see the README in this repository for the requirements of this lab exercise
# Justin Le
# lej42@uci.edu
# 50644854

def add(firstnum, secondnum):
    return firstnum + secondnum
def subtract(firstnum, secondnum):
    return firstnum - secondnum
def mutiply(firstnum, secondnum):
    return firstnum * secondnum

if __name__ == "__main__":
    print("Welcome to ICS 32 PyCalc!")
    print()
    firstnum = int(input("Enter your first operand: "))
    secondnum = int(input("Enter your second operand: "))
    operator = input("Enter your desired operator (+, -, or x): ")
    print()
    if operator == "+":
        print("The result of your calculation is:", add(firstnum, secondnum))
    elif operator == "-":
        print("The result of your calculation is:", subtract(firstnum, secondnum))
    elif operator == "x":
        print("The result of your calculation is:", mutiply(firstnum, secondnum))
    else:
        print("Invalid")
