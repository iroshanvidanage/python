def fibonacci_efficient(n):
    fibo = [0, 1]
    for i in range(2, n+1):
        fibo.append(fibo[i-1] + fibo[i-2])
    return fibo[n]

# for a in range(10):
#     print(fibonacci_efficient(a))


print(fibonacci_efficient(int(input())))
