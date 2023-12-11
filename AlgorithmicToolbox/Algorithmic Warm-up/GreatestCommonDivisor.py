def gcd_efficient(a, b):
    return a if b == 0 else gcd_efficient(b, a % b)

    # if b == 0:
    #     return a
    # else:
    #     return gcd_efficient(b, a % b)


a, b = map(int, input().split())
print(gcd_efficient(a, b))
