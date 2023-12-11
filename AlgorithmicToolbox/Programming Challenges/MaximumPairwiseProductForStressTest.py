def max_pair_product1(sys_input):
    # sorted_array = sorted(map(int, sys_input.split()), reverse=True)
    # sorted_array = sorted(list(dict.fromkeys(sys_input)), reverse=True)
    sorted_array = sorted(list(set(sys_input)), reverse=True)
    return sorted_array[0] * sorted_array[1]


def max_pair_product2(sys_input):
    n = len(sys_input)
    result = 0
    for _ in range(n):
        for __ in range(n):
            if (sys_input[_] * sys_input[__]) > result and sys_input[_] != sys_input[__]:
                result = (sys_input[_] * sys_input[__])
    return result


def max_pair_product3(sys_input):
    max1 = max2 = -1
    _: int
    for _ in sys_input:
        if max1 < _: max2, max1 = max1, _
        if max2 < _ < max1: max2 = _
    return max1 * max2

# print(max_pair_product("7 5 14 2 8 8 10 1 2 3"))
# input()
# print(max_pair_product(input()))
