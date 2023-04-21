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


matrix = Solution()

print(matrix.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
