import random

rand_num = random.random() * 10 + 2
print(rand_num)
a = [int(random.random() * 10000) for _ in range(int(rand_num))]
print(a)
# print(MaximumPairwiseProduct.max_pair_product(a))
