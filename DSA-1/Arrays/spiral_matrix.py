class Solution:
    def spiralOrder(self, matrix):
        left = 0
        right = len(matrix[0]) - 1
        top = 0
        bottom = len(matrix) - 1

        ans = []
        while left <= right and top <= bottom:
            for i in range(left, right + 1):
                ans.append(matrix[left][i])
            for i in range(top + 1, bottom + 1):
                ans.append(matrix[i][right])
            for i in range(right - 1, left - 1, -1):
                ans.append(matrix[bottom][i])
            for i in range(bottom - 1, top, -1):
                ans.append(matrix[i][top])
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        return ans


def generateSpiralMatrix(A):
    left = 0
    right = A - 1
    top = 0
    down = A - 1
    i = 0
    matrix = [[0 for _ in range(A)] for _ in range(A)]
    k = 1
    while left <= right and top <= down:
        for i in range(left, right + 1):
            matrix[top][i] = k
            k += 1
        for i in range(top + 1, down + 1):
            matrix[i][right] = k
            k += 1
        for i in range(right - 1, left - 1, -1):
            matrix[down][i] = k
            k += 1
        for i in range(down - 1, top, -1):
            matrix[i][left] = k
            k += 1
        left += 1
        right -= 1
        top += 1
        down -= 1
    return matrix


print(generateSpiralMatrix(3))

# matrix = Solution()
# print(matrix.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
