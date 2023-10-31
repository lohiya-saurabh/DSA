def solve(A):
    A.sort()
    minFlips = [[float('inf') for _ in range(sum(A)//2 + 1)] for _ in range(len(A) + 1)]
    for i in range(len(A) + 1):
        minFlips[i][0] = 0
    for i in range(1, len(A) + 1):
        for j in range(1, sum(A)//2 + 1):
            if j >= A[i - 1]:
                minFlips[i][j] = min(minFlips[i - 1][j], 1 + minFlips[i- 1][j - A[i - 1]])
            else:
                minFlips[i][j] = minFlips[i - 1][j]
    for i in range(len(minFlips[-1]) - 1, -1, -1):
        if minFlips[-1][i] != float('inf'):
            return minFlips[-1][i]
        


print(solve([8, 4, 5, 7, 6, 2]))

