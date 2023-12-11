def fibonacci_efficient(n, a):
    fibo = [0, 1]
    for i in range(2, n+1):
        fibo.append(fibo[i-1] + fibo[i-2])
    return fibo[n] % a


def fibonacci_efficient2(n, m):
    n = n % 60
    a, b = 0, 1
    if n < 1:
        return 0
    for i in range(2, n+1):
        a, b = b, (a + b) % m
    return b % m


def fibonacci_efficient3(n, m):
    a, b = 0, 1
    if n < 1:
        return 0
    for i in range(2, n+1):
        a, b = b, a + b
    return b % m


n, m = map(int, input().split())
print(fibonacci_efficient2(n, m))


# not working
