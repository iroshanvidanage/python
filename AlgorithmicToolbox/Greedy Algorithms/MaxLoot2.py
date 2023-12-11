[number_of_items, pack_capacity, *items_list] = map(int, input().split())
value = items_list[0:(2 * number_of_items + 2):2]
weights = items_list[1:(2 * number_of_items + 2):2]
lst = []
for i in range(number_of_items):
    lst.append((value[i], weights[i]))

lst.sort(key=lambda x: x[0]/x[1], reverse=True)

total_value = 0

for v, w in lst:
    if pack_capacity == 0:
        print(total_value)
        quit()
    amt = min(w, pack_capacity)
    total_value += amt*v/w
    pack_capacity -= amt

print(round(total_value, 4))
