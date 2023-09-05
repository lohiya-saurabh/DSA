def maxSum(A):
    max_sum = []
    for i in range(A[0]):
        max_sum.append(max(A[0][i], A[1][i]))
    t = 0
    for i in range(2, len(A)):
        max_till = max(max_till, max_sum[i - 2])
        t = max(t, max_till + max_sum[i])
    return t
