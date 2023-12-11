def knapsack(capacity, value_weights_dict, sorted_list, number_of_items):
    n = number_of_items
    value = 0
    i = 0
    while i < n:
        if capacity == 0:
            return value

        a = min(value_weights_dict[sorted_list[i]], capacity)
        value += a * sorted_list[i]
        capacity -= a
        # print(a, sorted_list[i], value_weights_dict[sorted_list[i]], value, capacity)
        i += 1

    return value


def unsorted_list(n):
    this_dict = {}
    for i in range(n):
        [value_of_item, weight] = map(int, input().split())
        this_dict.update({value_of_item/weight: weight})
    return this_dict, sorted(this_dict, reverse=True)


[number_of_items, pack_capacity, *items_list] = map(int, input().split())
value_weights, sorted_list_items = unsorted_list(number_of_items)
# print(sorted_list_items)
print(round(knapsack(pack_capacity, value_weights, sorted_list_items, number_of_items)), 3)
