def removeDuplicates(nums):
    i = 0
    j = 0
    while j < len(nums):
        count = 0
        while j < len(nums) and nums[i] == nums[j]:
            count += 1
            j += 1
        i += 1
        if count >= 1 and j < len(nums):
            nums[i] = nums[j]

    while i < len(nums):
        nums[i] = "_"
        i += 1
    return nums


def removeDuplicatesV2(nums):
    i, j = 0, 0
    while j < len(nums):
        count = 0
        while j < len(nums) and nums[i] == nums[j]:
            count += 1
            j += 1

        for k in range(min(2, count)):
            i += 1

        if j < len(nums):
            nums[i] = nums[j]

    while i < len(nums):
        nums[i] = "_"
        i += 1

    return nums


nums = [1, 2, 2, 3, 3, 3, 3, 4, 5, 5, 5]
print(removeDuplicatesV2(nums))
