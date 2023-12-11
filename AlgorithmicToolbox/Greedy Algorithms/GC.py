def points_cover_sorted(sorted_list):
    grouped_list = []
    i = 0
    n = len(sorted_list)

    while i < n:
        left_most = sorted_list[i]
        right_most = left_most + 1

        while i < n and sorted_list[i] <= right_most:
            i += 1

        grouped_list.append(sorted_list[sorted_list.index(left_most):i])

    return grouped_list


x = [3, 3.5, 3.6, 5, 5.2, 6, 8, 8.1, 8.3, 8.6, 8.7, 8.8, 9.5, 10]

print(points_cover_sorted(x))

