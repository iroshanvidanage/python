import random


def rand_quick_sort(arr, low, high):
    if low >= high:
        return
    k = random.randint(low, high)
    # tem = arr[low]
    # arr[low] = arr[k]
    # arr[k] = tem
    arr[low], arr[k] = arr[k], arr[low]

    m = partition(arr, low, high)

    rand_quick_sort(arr, low, m - 1)
    rand_quick_sort(arr, m + 1, high)


def partition(arr, low, high):
    x = arr[low]
    j = low

    for i in range(low + 1, high):
        if arr[i] <= x:
            arr[i], arr[j] = arr[j], arr[i]
            j = j + 1

    arr[low], arr[j] = arr[j], arr[low]

    return j

