def medianOfTwoSortedArrays(arr1, arr2):
    n1, n2 = len(arr1), len(arr2)
    middle = (n1 + n2 + 1)//2
    left, right = 0, min(middle, n1)

    while left <= right:
        partition1 = (left + right + 1)//2
        partition2 = middle - partition1
        l1 = arr1[partition1 - 1] if partition1 > 0 else float('-inf')
        l2 = arr2[partition2 - 1] if partition2 > 0 else float('-inf')
        r1 = arr1[partition1] if partition1 < n1 else float('inf')
        r2 = arr2[partition2] if partition2 < n2 else float('inf')
        if l1 <= r2 and l2 <= r1:
            if (n1 + n2) % 2 == 0:
                return ((max(l1, l2) + min(r1, r2))/2)
            else:
                return max(l1, l2)
        elif l1 > r2:
            right = partition1 - 1
        else:
            left = partition1 + 1
    return -1


arr1 = [1, 4, 6, 7, 8, 10, 12, 13, 14]
arr2 = [2, 5, 7]

print(medianOfTwoSortedArrays(arr1, arr2))
