def minSumOfMountainTriplets(arr):
    i, j , k = 0, 1, len(arr) - 1
    minSum = float('inf')
    while i < k:
        for j in range(i + 1, k, 1):
            if arr[j] > arr[i] and arr[j] > arr[k]:
                minSum = min(minSum, arr[i] + arr[j] + arr[k])
            if arr[j] < arr[i]:
                i = j
                break
        i += 1
    while i < k:
        for j in range(k - 1, i, -1):
            