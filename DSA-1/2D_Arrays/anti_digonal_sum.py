def diagonal(A):
    row, col = len(A), len(A[0])
    anti_digonal_arrays = []
    i, j, k = 0, 0, 0
    while k < row + col - 1:
        tmp_row, tmp_col = i, j
        curr_digonal = []
        for m in range(row):
            if tmp_row >= 0 and tmp_row < row and tmp_col >= 0 and tmp_col < col:
                curr_digonal.append(A[tmp_row][tmp_col])
            else:
                curr_digonal.append(0)
            tmp_row += 1
            tmp_col -= 1
        anti_digonal_arrays.append(curr_digonal)
        if j == col - 1:
            i += 1
        else:
            j += 1
        k += 1
    return anti_digonal_arrays


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(diagonal(matrix))
