def max_pair_product(sys_input):
    sorted_array = sorted(map(int, sys_input.split()), reverse=True)
    return sorted_array[0] * sorted_array[1]

# print(max_pair_product("7 5 14 2 8 8 10 1 2 3"))
input()
print(max_pair_product(input()))
