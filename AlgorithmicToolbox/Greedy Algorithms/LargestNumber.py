def largest_number(arr):
    if arr is not None and len(arr) != 0:
        a = max(arr)
        arr.remove(a)
        return str(a) + largest_number(arr)
    else:
        return ''


input()
ar = list(map(int, input().split()))
for i in ar:
    if i < 10:
        arr = [str(x) for x in ar]
        ar = [int(x) for x in ''.join(arr)]
# ar = [3, 5, 9, 6, 7, 9, 6, 8, 1, 3, 5, 8, 7, 6, 3, 7, 5, 6, 3, 7, 5, 9, 7, 6, 7, 1, 2, 3, 6, 4, 8]
# print(arr, ar)
print(largest_number(ar))
