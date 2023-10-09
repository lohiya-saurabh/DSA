def unique_paths(matrix):
    start_row = -1
    start_col = -1
    total_zeros = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                start_row = i
                start_col = j
            elif matrix[i][j] == 0:
                total_zeros += 1
    return unique_paths_helper(matrix, start_row, start_col, total_zeros + 1)


def unique_paths_helper(matrix, start_row, start_col, total_zeros):
    if start_row < 0 or start_row >= len(matrix) or start_col < 0 or start_col >= len(matrix[0]) or matrix[start_row][start_col] == -1:
        return 0
    if matrix[start_row][start_col] == 2:
        if total_zeros == 0:
            return 1
        return 0
    # tmp = matrix[start_row][start_col]
    matrix[start_row][start_col] = -1
    paths = unique_paths_helper(matrix.copy(), start_row + 1, start_col, total_zeros - 1) + unique_paths_helper(
        matrix.copy(), start_row - 1, start_col, total_zeros - 1) + unique_paths_helper(matrix.copy(), start_row, start_col + 1, total_zeros - 1) + unique_paths_helper(matrix.copy(), start_row, start_col - 1, total_zeros - 1)
    matrix[start_row][start_col] = 0
    return paths


print(unique_paths([[1, 0, -1], [2, 0, 0]]))
