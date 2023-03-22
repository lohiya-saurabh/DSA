def threeSum(nums):
    i = 0
    k = len(nums) - 1
    nums.sort()
    ans = []
    while i < k:
        j = i + 1
        while j < k:
            tmp = nums[i] + nums[j] + nums[k]
            if tmp == 0 and not ([nums[i], nums[j], nums[k]] in ans):
                ans.append([nums[i], nums[j], nums[k]])
            if tmp == 0:
                j += 1
                k -= 1
            elif tmp < 0:
                j += 1
            elif tmp > 0:
                k -= 1
        i += 1
    return ans


print(threeSum(nums=[-1, 0, 1, 2, -1, -4]))
