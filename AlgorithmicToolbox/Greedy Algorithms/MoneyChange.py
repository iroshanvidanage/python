def money_change(n):
    count = 0
    for i in [10, 5, 1]:
        count += n // i
        n %= i
        if n == 0:
            return count


n = int(input())
print(money_change(n))
