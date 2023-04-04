def rangeSum(A, B):
    prefSum = [0] * (len(A) + 1)
    ans = []
    currSum = 0
    for i in range(1, len(A) + 1):
        prefSum[i] = prefSum[i - 1] + A[i - 1]

    for arr in B:
        ans.append(prefSum[arr[1] + 1] - prefSum[arr[0]])
    return ans


rangeSum([1, 3, 4, 6, 8], [[2, 4]])
