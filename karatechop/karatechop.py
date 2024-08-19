# binary search


def karate_chop(int_in, arr_int):
    mid = len(arr_int)//2
    # print(mid, arr_int[mid])
    if int_in < arr_int[0] or int_in > arr_int[-1]:
        print(-1)
    elif int_in == arr_int[mid]:
        # print('Clause1', mid)
        print(mid)
    elif int_in > arr_int[mid]:
        karate_chop(int_in, arr_int[mid + 1:])
        # print('Clause2', arr_int[mid + 1:])
    elif int_in < arr_int[mid]:
        karate_chop(int_in, arr_int[:mid])
        # print('Clause3', arr_int[:mid])
    else:
        print(-1)
        # return -1


arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
arr3 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

