def longestIncreasingSubsequence(A):
    stack = []
    maxLis = 0
    for i in range(len(A)):
        while stack and stack[-1] >= A[i]:
            stack.pop()
        stack.append(A[i])
        maxLis = max(maxLis, len(stack))
    return maxLis


print(longestIncreasingSubsequence([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))