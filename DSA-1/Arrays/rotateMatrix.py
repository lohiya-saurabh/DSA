def rotateMatrix(A):
    for i in range(len(A)):
        for j in range(i+1, len(A[0])):
            [A[i][j], A[j][i]] = [A[j][i], A[i][j]]

    for i in range(len(A)):
        A[i] = A[i][::-1]
    return A


print(rotateMatrix([[1, 2], [3, 4]]))
