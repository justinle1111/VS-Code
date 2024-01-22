def generate_fibonacci (n):
    fib_nums = [0, 1]

    for i in range(2, n):
        next = fib_nums[i - 1] + fib_nums[i - 2] #each new number is the sum of past two numbers
        fib_nums.append(next)
    
    return fib_nums

def generate_fibonacci_recursive (n):
    #base case
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_seq = generate_fibonacci_recursive (n - 1)
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq
if __name__ == "__main__":
    print(generate_fibonacci(10))
    print(generate_fibonacci_recursive(10))
