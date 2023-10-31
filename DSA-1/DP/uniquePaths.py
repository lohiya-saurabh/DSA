def uniquePathsWithObstacles(A):
    uniquePaths = [[0 for _ in range(len(A[0]))] for _ in range(len(A))]
    foundObstacle = False
    for i in range(len(A[0])):
        if A[0][i] == 1:
            foundObstacle = True
        if not foundObstacle:
            uniquePaths[0][i] = 1
    foundObstacle = False
    for i in range(len(A)):
        if A[i][0] == 1:
            foundObstacle = True
        if not foundObstacle:
            uniquePaths[i][0] = 1
    for i in range(1, len(A)):
        for j in range(1, len(A[0])):
            if A[i][j] == 0:
                horizontalPaths = uniquePaths[i - 1][j] if i - 1 >= 0 else 0
                verticalPaths = uniquePaths[i][j - 1] if j - 1 >= 0 else 0
                uniquePaths[i][j] = horizontalPaths + verticalPaths
    return uniquePaths[-1][-1]


print(uniquePathsWithObstacles([[0, 0, 1, 0, 1, 1, 1, 1], [
      0, 1, 0, 1, 0, 0, 1, 1], [0, 0, 1, 0, 0, 0, 0, 1]]))
