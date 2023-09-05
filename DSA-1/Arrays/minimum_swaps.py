def minimum_swaps(A, B):
    n = len(A)
    k = 0
    closest = 0
    current_closest = 0
    for i in range(n):
        if A[i] <= B:
            k += 1
    for i in range(k):
        if A[i] <= B:
            closest += 1
    for i in range(n - k):
        current = 0
        if A[k + i] <= B:
            current += 1
        if A[i] <= B:
            current -= 1
        current_closest += current
        closest = max(closest, current_closest)
    return k - closest


print(minimum_swaps([1, 12, 10, 3, 14, 10, 5, 2, 9, 2], 8))
