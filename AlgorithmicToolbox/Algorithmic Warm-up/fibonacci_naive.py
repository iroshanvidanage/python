def fibonacci_naive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)


print(fibonacci_naive(int(input())))
