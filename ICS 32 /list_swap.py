def main():
    list_a = [1, 3, 4, 5, 11]
    list_b = [11, 30, 40, 5]
    list_swap (list_a, list_b)
    print("Old List A:", list_a)
    print("Old List B:", list_b)

def list_swap (a, b):
    c = a
    a = b
    b = c

    print("In list_swap: ")
    print("New List A:", a)
    print("New List B:", b)

main()