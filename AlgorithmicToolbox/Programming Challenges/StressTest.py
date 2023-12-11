import random
import MaximumPairwiseProductForStressTest as mpp
counter = 0
# last ran 311812 test cases
# depending on the requirements the modifications can be different
while True:

    print("Test Case: ", counter)
    rand_num = random.random() * 10 + 2
    print(rand_num)
    a = [int(random.random() * 10000) for _ in range(int(rand_num))]
    print(a)
    a1 = mpp.max_pair_product1(a)
    a2 = mpp.max_pair_product2(a)
    a3 = mpp.max_pair_product3(a)
    if a1 != a2 or a2 != a3 or a1 != a3:
        print("Wrong", a1, a2, a3)
        break
    else:
        print("OK")
    counter += 1



