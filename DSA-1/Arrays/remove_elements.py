A = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]


def removeElement(nums, val):
    i = 0
    j = len(nums) - 1
    count = 0
    n = len(nums)
    while i < j:
        while i < n and nums[i] != val:
            i += 1

        while j > -1 and nums[j] == val:
            nums[j] = "_"
            j -= 1

        if i < j:
            nums[i] = nums[j]
            nums[j] = "_"
            count += 1
    return nums


print(removeElement([3, 2, 2, 3], 3))
