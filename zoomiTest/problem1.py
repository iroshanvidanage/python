
def maxAndSecondMax(arr, len):
    max1 = None
    max2 = None

    for i in arr:
        if max1 is None or max1 < i:
            max2, max1 = max1, i
        if (max2 is None or max2 < i) and (i < max1):
            max2 = i
    return max1, max2


#array1 = [10, 2, 3, 45, 5, 6]

#print(maxAndSecondMax(array1,6))

