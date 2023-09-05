def largestNumber(A, B):
    sorted_A = sorted(A)[::-1]
    swaps = 0
    dict_A = {}
    n = len(A)
    for i in range(n):
        dict_A[A[i]] = i
    i = 0
    while swaps < B and i < n:
        if sorted_A[i] != A[i]:
            tmp = A[i]
            A[i] = sorted_A[i]
            A[dict_A[sorted_A[i]]] = tmp
            swaps += 1
            dict_A[tmp] = dict_A[sorted_A[i]]
        i += 1
    return A


print(largestNumber([3, 2, 4, 1, 5], 3))
