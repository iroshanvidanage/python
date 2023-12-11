def majority_element(n, arr):
    n = n / 2
    count_dict = {}
    for key in arr:
        if key in count_dict:
            count_dict[key] += 1
        else:
            count_dict.update({key: 1})

    count_list = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)

    return 1 if count_list[0][1] > n else 0


numb = int(input())
ar = [int(x) for x in input().split()]

print(majority_element(numb, ar))
