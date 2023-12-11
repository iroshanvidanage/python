import math

n = int(input())

num_operations = [0, 0] + [math.inf] * (n - 1)

for i in range(2, n + 1):
    temp_1, temp_2, temp_3 = [math.inf] * 3

    temp_1 = num_operations[i - 1] + 1

    if i % 2 == 0: temp_2 = num_operations[i // 2] + 1
    if i % 3 == 0: temp_3 = num_operations[i // 3] + 1
    min_ops = min(temp_1, temp_2, temp_3)
    num_operations[i] = min_ops

print(num_operations[n])

nums = [n]

while n != 1:
    if n % 3 == 0 and num_operations[n] - 1 == num_operations[n // 3]:
        nums += [n // 3]
        n //= 3
    elif n % 2 == 0 and num_operations[n] - 1 == num_operations[n // 2]:
        nums += [n // 2]
        n //= 2
    else:
        nums += [n-1]
        n -= 1

print(' '.join([str(i) for i in nums][::-1]))


