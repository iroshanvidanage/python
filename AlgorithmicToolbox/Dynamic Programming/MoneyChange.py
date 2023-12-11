import math


def change_money(money):
    change = [1, 3, 4]
    min_coins = [0] + [math.inf] * money

    for i in range(1, money+1):
        for j in change:
            if i >= j:
                coins = min_coins[i - j] + 1
                if coins < min_coins[i]:
                    min_coins[i] = coins

    return min_coins[money]


in_money = int(input())

print(change_money(in_money))

