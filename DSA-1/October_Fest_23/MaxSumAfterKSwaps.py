def maxSumAfterKSwaps(A, B, K):
    newArr = [[A[i], B[i], A[i] - B[i]] for i in range(len(A))]
    newArr.sort(key= lambda x: x[2], reverse=True)
    maxSum = sum(A)
    K = K %(len(A) + 1)
    i = 0
    while i < K and newArr[-1][2] < 0:
        maxSum += newArr[-1][2]* (-1)
        newArr.pop()
        i += 1
    return maxSum
        
print(maxSumAfterKSwaps([1, 3, 1, 3, 1], [2, 4, 1, 6, 5], 3))