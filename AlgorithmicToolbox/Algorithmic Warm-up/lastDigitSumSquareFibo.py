def fibonacci_efficient(n):
    fibo = [0, 1]
    if n < 1:
        return 0
    for i in range(2, n+1):
        fibo.append(pow(fibo[i-1] + fibo[i-2], 2))
    return sum(fibo)


def fibonacci_efficient2(n):
    n = n % 60

    a, b = 0, 1
    total_sum = 1
    if n < 1:
        return 0
    for i in range(2, n+1):
        a, b = b, (a + b) % 10
        total_sum = (total_sum + b*b) % 10
    return total_sum % 10


print(fibonacci_efficient2(int(input())))
