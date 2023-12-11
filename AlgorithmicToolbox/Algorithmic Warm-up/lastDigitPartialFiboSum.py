def fibonacci_efficient(a, n):
    fibo = [0, 1]
    for i in range(2, n+1):
        fibo.append(fibo[i-1] + fibo[i-2])
    return sum(fibo[a:n + 1]) % 10


def fibonacci_efficient2(m, n):
    n = n % 60
    m = m % 60
    a, b = 0, 1
    if m < 2:
        total_sum = 1
    else:
        total_sum = 0
    if n < 1:
        return 0
    for i in range(2, n + 1):
        a, b = b, (a + b) % 10
        if i >= m:
            total_sum = (total_sum + b) % 10
    return total_sum % 10

def fibonacci_efficient3(m, n):
    n = n % 60
    m = m % 60
    #print(m, n)
    if m > n:
        return (fibonacci_efficient2(0, n) + fibonacci_efficient2(m, 59)) % 10
    else:
        return fibonacci_efficient2(m, n)


a, n = map(int, input().split())
#a = 5618252
#n = 6583591534156
print(fibonacci_efficient3(a, n))
