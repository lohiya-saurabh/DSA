def transposeMatrix(matrix):
    row, col = len(matrix), len(matrix[0])
    transpose_matrix = [[0 for _ in range(row)] for _ in range(col)]
    for j in range(col):
        for i in range(row):
            transpose_matrix[j][i] = matrix[i][j]
    return transpose_matrix


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(transposeMatrix(matrix))
