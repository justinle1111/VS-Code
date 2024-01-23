#lab4.py

# Starter code for lab 4 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.
# Please see the README in this repository for the requirements of this lab exercise

# Justin Le
# lej42
# 50644854

import random

"""
The default numbers here are generally good enough to create a rich tree. 
You are free to play with the numbers if you want. Lower numbers will simplify the results, 
larger numbers will take more time to render and create hundreds of acorns.
"""

TREE_DEPTH = 5
NODE_DEPTH = 5

def tree_builder(nodes:list, level:int, acorn:str) -> list:
    """
    Builds a tree using the random integers selected from the tree_depth and node_depth defaults
    """
    r = random.randrange(1, NODE_DEPTH)
    for i in range(r):
        if level < TREE_DEPTH:
            level_id  = f"L{level}-{i}"
            if level_id == acorn:
                level_id += "(acorn)"
            n = [level_id]
            nodes.append(tree_builder(n, level+1, acorn_placer()))

    return nodes

def acorn_placer() -> str:
    """
    Returns a random acorn location based on tree_depth and node_depth defaults
    """
    return f"L{random.randrange(1,TREE_DEPTH)}-{random.randrange(1,NODE_DEPTH)}"

def find_acorn(tree, root):
    root = []
    for level in tree:
        if type(level) == list:
            root.append(level[0])
            find_acorn(level, root)
        else:
            if "(acorn)" in level:
                print("This acorn is in this", level)
    return root

def run():
    # create a tree and start placing acorns
    tree = tree_builder([], 1, acorn_placer())
    # print the tree for testing. 
    # TODO: REMOVE THIS PRINT STATEMENT BEFORE YOU SUBMIT YOUR LAB
    print(tree)
    
    # insert your solution code here

    find_acorn(tree, [])
    # end solution

if __name__ == "__main__":
    print("Welcome to PyAcornFinder! \n")

    run()
