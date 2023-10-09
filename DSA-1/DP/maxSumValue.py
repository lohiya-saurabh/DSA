def solve(A, B, C, D):
    dp = [[float('-inf'), float('-inf'), float('-inf')]
          for _ in range(len(A) + 1)]
    for i in range(1, len(A) + 1):
        dp[i][0] = max(dp[i - 1][0], A[i - 1]*B)
        dp[i][1] = max(dp[i - 1][1], dp[i][0] + A[i - 1]*C)
        dp[i][2] = max(dp[i - 1][2], dp[i][1] + A[i - 1]*D)
    return dp[len(A)][2]


print(solve([-44, -41, 1, -26], 29, -15, 27))
