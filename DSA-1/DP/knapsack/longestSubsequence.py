def lengthOfLongestSubsequence( nums, target):
    n = len(nums)
    dp = [[-1] * (sum + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        dp[i][0] = 0
    
    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= nums[i - 1] and dp[i - 1][j - nums[i - 1]] != -1:
                dp[i][j] = max(1 + dp[i - 1][j - nums[i - 1]], dp[i][j])
    
    return dp[n][sum]


print(lengthOfLongestSubsequence([4,1,3,2,1,5], 7))