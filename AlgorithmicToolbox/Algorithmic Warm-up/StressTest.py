import random
import FiboAgainHuge as fibb
import lastDigitSumFibo as fibbsum
import threading
import time

# counter1 = 1
# counter2 = 1
counter3 = 1

#
# def route1():
#     while True:
#         n = int(random.random() * 1000000) + 1
#         m = int(random.random() * 10) + 1
#
#         global counter1
#         print("Test Case: ", counter1)
#         print(n, m)
#         a1 = fibb.fibonacci_efficient2(n, m)
#         # a2 = fibb.fibonacci_efficient3(n, m)
#
#         print("Function 1", a1)
#
#         counter1 += 1
#         time.sleep(1)
#
#
# def route2():
#     while True:
#         n = int(random.random() * 1000000) + 1
#         m = int(random.random() * 10) + 1
#
#         global counter2
#         print("Test Case: ", counter2)
#         print(n, m)
#         # a1 = fibb.fibonacci_efficient2(n, m)
#         a2 = fibb.fibonacci_efficient3(n, m)
#
#         print("Function 2", a2)
#
#         counter2 += 1
#         time.sleep(1)
#
#
# th1 = threading.Thread(target=route1())
# th2 = threading.Thread(target=route2())

while True:
    n = int(random.random() * 10000000000) + 1

    print("Test Case: ", counter3)
    print(n)
    a1 = fibbsum.fibonacci_efficient2(n)
    a2 = fibbsum.fibonacci_efficient3(n)

    if a1 != a2:
        print("Wrong", a1, a2)
        break
    else:
        print("OK", a1, a2)

    counter3 += 1

