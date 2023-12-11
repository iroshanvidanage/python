import random


def rand_quick_sort3(arr, low, high):
    if low + 1 >= high:
        return

    k = random.randint(low, high - 1)

    arr[low], arr[k] = arr[k], arr[low]

    m1, m2 = partition3(arr, low, high)

    rand_quick_sort3(arr, low, m1)
    rand_quick_sort3(arr, m2 + 1, high)


def partition3(arr, low, high):
    m2 = low
    for i in range(low + 1, high):
        if arr[i] <= arr[low]:
            arr[m2 + 1], arr[i] = arr[i], arr[m2 + 1]
            m2 += 1

    arr[low], arr[m2] = arr[m2], arr[low]

    m1 = low
    for i in range(low, m2):
        if arr[i] < arr[m2]:
            arr[i], arr[m1] = arr[m1], arr[i]
            m1 += 1

    return m1, m2


numb = int(input())
ar = [int(x) for x in input().split()]
rand_quick_sort3(ar, 0, numb)
print(' '.join([str(x) for x in ar]))
