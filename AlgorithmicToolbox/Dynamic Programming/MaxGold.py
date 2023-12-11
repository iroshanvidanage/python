def max_weight(capacity, items):
    n = len(items)
    T = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            T[i][w] = T[i - 1][w]
            if w >= items[i - 1]:
                weight = T[i - 1][w - items[i - 1]] + items[i - 1]
                if weight > T[i][w]:
                    T[i][w] = weight
    # print(T)
    return T[n][capacity]


def optimal_solution(T, capacity, items):
    n = len(items)
    i = n
    w = capacity
    used_items = []
    while i > 0 and w > 0:
        if T[i][w] == T[i - 1][w]:
            i = i - 1
        else:
            used_items.append(i - 1)
            w = w - items[i - 1]
            i = i - 1
    return used_items


W, n = map(int, input().split())
weights = [int(_) for _ in input().split()]
print(max_weight(W, weights))
