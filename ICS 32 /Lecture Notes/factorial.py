def factorial (n):
    if n == 0: # base case
        return 0
    elif n == 1:
        return 1
    elif n < 0:
        raise TypeError("Number must be positive!")
    else: # recursive case
        return n * factorial(n - 1)


if __name__ == "__main__":
    try:
        value = factorial(5)
        print(value)
    except TypeError as e:
        print(e)
    else:
        print(value)