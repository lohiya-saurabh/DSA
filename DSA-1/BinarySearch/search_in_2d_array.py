def searchMatrix(matrix, target):
    i, j = 0, len(matrix[0]) - 1
    dir = "horizontal"
    start, end = i, j
    return __binarySearchHelper(i, j, start, end, matrix, target, dir)


def __binarySearchHelper(i, j, start, end, matrix, target, dir):
    if i >= len(matrix) or j < 0:
        return False
    if dir == "horizontal":
        arr = matrix[i]
    else:
        arr = [matrix[x][j] for x in range(len(matrix))]

    middle = (start + end)//2
    while start <= end:
        middle = (start + end)//2
        if arr[middle] < target:
            start = middle + 1
        elif arr[middle] > target:
            end = middle - 1
        else:
            return True

    if dir == "horizontal":
        dir = "vertical"
        return __binarySearchHelper(i + 1, middle, i + 1, len(matrix) - 1, matrix, target, dir)
    if dir == "vertical":
        dir = "horizontal"
        return __binarySearchHelper(middle, j - 1, 0, j - 1, matrix, target, dir)


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
target = 10

print(searchMatrix(matrix, target))
