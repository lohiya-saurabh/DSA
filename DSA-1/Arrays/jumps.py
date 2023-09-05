def jump(nums):
    N = len(nums)
    if N <= 1:
        return 0

    jumps = 0
    curr_end = 0
    max_reach = 0

    for i in range(N - 1):
        max_reach = max(max_reach, i + nums[i])

        if i == curr_end:
            jumps += 1
            curr_end = max_reach

        if curr_end >= N - 1:
            return jumps

    return -1


arr = [2, 2, 1, 1, 4]

print(jump(arr))
