import time
import gcd_naive as gcd


def lcm_naive(a, b):
    if a * b == 1:
        return 1
    if a > b:
        greater = a
    else:
        greater = b
    while True:
        if greater % a == 0 and greater % b == 0:
            return greater
        greater += 1


def lcm_eff(a, b):
    if a * b == 1:
        return 1
    else:
        return (a * b) / gcd.gcd_naive(a, b)


a, b = map(int, input().split())
# start = time.time()
# print(lcm_naive(a, b))
print(lcm_eff(a, b))
# print(time.time()-start)

# not working correctly
