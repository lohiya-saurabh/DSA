class Matrix:
    # @param A : list of list of integers
    # @return the same list modified
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])

    def rotateMatrix(self):
        self.transposeOfMatrix()
        self.inverseOfMatrix()
        return self.matrix

    def transposeOfMatrix(self):
        for i in range(self.rows):
            for j in range(i + 1, self.cols):
                self.matrix[i][j], self.matrix[j][i] = self.matrix[j][i], self.matrix[i][j]
        return self.matrix

    def inverseOfMatrix(self):
        for i in range(self.rows):
            for j in range(self.cols//2):
                self.matrix[i][j], self.matrix[i][self.cols - j -
                                                  1] = self.matrix[i][self.cols - j - 1], self.matrix[i][j]
        return self.matrix


matrix = [
    [1, 2],
    [3, 4]
]

matrixT = Matrix(matrix)

print(matrixT.rotateMatrix())
