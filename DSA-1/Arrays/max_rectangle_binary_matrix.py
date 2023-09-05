
def maximalRectangle(A):
    rows = len(A)
    cols = len(A[0])
    maxRectangleSize = [[0 for _ in range(cols)] for _ in range(rows)]
    maxRectSize = 0
    for i in range(rows):
        one_count = 0
        for j in range(cols):
            if A[i][j] == 1:
                maxRectangleSize[i][j] = one_count + 1
                one_count += 1
            else:
                one_count = 0
            maxRectSize = max(maxRectSize, maxRectangleSize[i][j])
    for i in range(cols):
        one_count = 0
        rectSizes = float('inf')
        for j in range(rows):
            if maxRectangleSize[j][i] >= 1:
                one_count += 1
                rectSizes = min(rectSizes, maxRectangleSize[j][i])
                maxRectangleSize[j][i] = max(
                    maxRectangleSize[j][i], rectSizes*one_count)
            else:
                rectSizes = float('inf')
                one_count = 0
            maxRectSize = max(maxRectSize, maxRectangleSize[j][i])
    for i in range(rows):
        print(maxRectangleSize[i])
    return maxRectSize


matrix = [
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0],
    [1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1]
]

matrix2 = [
    [0, 0, 1, 0, 0, 0, 1, 0, 1],
    [0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 1, 0, 1],
    [0, 1, 0, 0, 0, 1, 1, 0, 1],
    [0, 1, 0, 0, 0, 0, 1, 1, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 0, 1, 0, 1]
]

print(maximalRectangle(matrix2))
