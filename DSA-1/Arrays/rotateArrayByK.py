def rotateArray(arr, k):
    n = len(arr)
    k = k % n
    arr = reverseArray(arr, 0, n - 1)
    arr = reverseArray(arr, 0, k - 1)
    arr = reverseArray(arr, k, n - 1)
    return arr


def reverseArray(arr, i, j):
    while i < j:
        [arr[i], arr[j]] = [arr[j], arr[i]]
        i += 1
        j -= 1
    return arr


print(rotateArray([3, 4, 2, -7, 8, 5, 1], 2))

# 3 4 2 -7 8 5
# 5 8 -7 2 4 3
# -7 8 5 3 4 2
