def fibonacci_efficient(n):
    if n <= 1:
        return n

    a, b = 0, 1

    for i in range(n - 1):
        a, b = b, (a + b) % 10
    return b


arr = []
for _ in range(121):
    l = fibonacci_efficient(_)
    k = l % 10
    arr.append([_, l, l * l, (l * l) % 10, k, k * k, (k * k) % 10])
    #print(arr[_])

arr2 = [0, 0, 0, 0, 0, 0]
arr3 = [0, 0, 0, 0, 0, 0]
for j in range(len(arr)):
    for i in range(len(arr2)):
        arr2[i] += int(arr[j][i+1])
        arr3[i] = (arr3[i] + int(arr[j][i+1])) % 10
    print(arr[j][0])
    print(arr2)
    print(arr3)

# every 60 terms the sequence is repeated