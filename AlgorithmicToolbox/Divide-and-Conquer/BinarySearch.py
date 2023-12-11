def binary_search(arr, low, high, key):
    # input array is sorted
    if high < low:
        return -1

    mid = low + (high - low) // 2
    
    if arr[mid] == key:
        return mid
    elif arr[mid] > key:
        return binary_search(arr, low, mid - 1, key)
    else:
        return binary_search(arr, mid + 1, high, key)


# ar = [1, 2, 3, 4, 5, 8, 10, 12, 15, 18, 19, 21, 22, 24, 29, 33, 36, 38, 41, 46, 51, 52, 53, 58, 60]
# se = [8, 9, 60, 20, 11]
high = int(input())
ar = [int(x) for x in input().split()]
low = 0
int(input())
se = [int(x) for x in input().split()]
out = []
for key1 in se:
    out.append(str(binary_search(ar, low, high - 1, key1)))

print(' '.join(out))
