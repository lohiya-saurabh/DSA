def maxSubArray(A):
    max_sum = float('-inf')
    n = len(A)
    max_s = [0]*n
    curr_sum = 0
    for i, num in enumerate(A):
        curr_sum = curr_sum + num
        max_s[i] = max(num, curr_sum)
        max_sum = max(max_sum, max_s[i])
        if curr_sum < 0:
            curr_sum = 0
    return max_sum


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(arr))
