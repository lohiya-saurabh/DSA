def longest_increasing_subsequence(arr):
    tails = []
    for x in arr:
        i = binary_search(tails, 0, len(tails), x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)


def binary_search(arr, l, r, x):
    while l < r:
        mid = (l+r)//2
        if arr[mid] > x:
            r = mid
        else:
            l = mid + 1
    return r


print(longest_increasing_subsequence([1, 7, 8, 9, 4, 4, 6, 8]))
