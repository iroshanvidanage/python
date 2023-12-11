import time


def fibonacci_efficient(n):
    if n <= 1:
        return n

    a, b = 0, 1

    for i in range(n -1):
        a, b = b, (a + b) % 10
    return b


#start = time.time()
print(fibonacci_efficient(int(input())))
#print(time.time()-start)
