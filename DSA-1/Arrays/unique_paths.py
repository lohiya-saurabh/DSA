
def uniquePathsWithObstacles(A):
    cols = len(A[0])
    rows = len(A)
    ways = [[0 for _ in range(cols)] for _ in range(rows)]
    flag = False
    if len(A) > 0:
        if A[0][0] == 1:
            return 0
    if rows == 1 and cols == 1:
        return 1 if A[0][0] == 0 else 0
    for i in range(1, cols):
        if flag:
            ways[0][i] = 0
        elif A[0][i - 1] == 1 or A[0][i] == 1:
            flag = True
        else:
            ways[0][i] = 1
    flag = False
    for i in range(1, rows):
        if flag:
            ways[i][0] = 0
        elif A[i - 1][0] == 1 or A[i][0] == 1:
            flag = True
        else:
            ways[i][0] = 1
    for i in range(1, rows):
        for j in range(1, cols):
            if A[i][j] == 0:
                ways[i][j] = ways[i - 1][j] + ways[i][j - 1]
            else:
                ways[i][j] = 0
    return ways[rows - 1][cols - 1]


matrix = [[0, 0], [0, 0], [0, 0], [1, 0], [0, 0]]

print(uniquePathsWithObstacles(matrix))
