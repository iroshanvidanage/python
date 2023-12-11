def knapsack(capacity, sorted_list, value_weights_dict):
    n = len(sorted_list)
    included_weights = [0] * n
    value = 0
    i = 0
    while i < n:
        if capacity == 0:
            return value, included_weights

        a = min(value_weights_dict[sorted_list[i]], capacity)
        value += a * sorted_list[i]
        capacity -= a
        included_weights[i] = a

    return value, included_weights
