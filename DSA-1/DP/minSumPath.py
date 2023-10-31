def minPathSum(A):
    minSumPath = [[0 for _ in range(len(A[0]))] for _ in range(len(A))]
    currSum = 0
    for i in range(len(A[0])):
        currSum += A[0][i]
        minSumPath[0][i] = currSum
    currSum = 0
    for i in range(len(A)):
        currSum += A[i][0]
        minSumPath[i][0] = currSum
    for i in range(1, len(A)):
        for j in range(1, len(A[0])):
            minSumPath[i][j] = min(minPathSum[i - 1][j],
                                   minPathSum[i][j - 1]) + A[i][j]
    return minSumPath[-1][-1]


print(minPathSum([[1, -3, 2], [2, 5, 10], [5, -5, 1]]))
