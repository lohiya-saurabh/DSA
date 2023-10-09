def NQueens(n):
    # The N-queens puzzle is the problem of placing N queens on an N×N chessboard such that no two queens attack each other.
    board = [[False for i in range(n)] for j in range(n)]
    cols = [False for i in range(n)]
    digonals = [False for i in range(2*n-1)]
    anti_digonals = [False for i in range(2*n-1)]
    return NQueensHelper(board, 0, n, cols, digonals, anti_digonals, [])


def NQueensHelper(board, i, n, cols, digonals, anti_digonals, res):
    if (i == n):
        res.append(board)
        return res
    for j in range(n):
        if (cols[j] or digonals[i+j] or anti_digonals[i-j+n-1]):
            continue
        cols[j] = True
        digonals[i+j] = True
        anti_digonals[i-j+n-1] = True
        board[i][j] = True
        res = NQueensHelper(board.copy(), i+1, n, cols.copy(),
                            digonals.copy(), anti_digonals.copy(), res)
        cols[j] = False
        digonals[i+j] = False
        anti_digonals[i-j+n-1] = False
        board[i][j] = False
    return res


print(NQueens(4))
