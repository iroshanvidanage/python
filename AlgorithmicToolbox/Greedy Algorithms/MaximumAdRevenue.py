n = int(input())
a = sorted(map(int, input().split()))
b = sorted(map(int, input().split()))

total_sum = sum([a[i]*b[i] for i in range(n)])
print(total_sum)
