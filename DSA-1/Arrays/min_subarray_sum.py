def minSubarraySum(nums, target):
    min_subarray_length = float('inf')
    subarray_sum = 0
    i, j = 0, 0
    while i < len(nums) and j < len(nums):
        subarray_sum += nums[j]
        if subarray_sum >= target:
            min_subarray_length = min(min_subarray_length, j - i + 1)
            subarray_sum -= nums[i]
            subarray_sum -= nums[j]
            i += 1
        else:
            j += 1

    return min_subarray_length if min_subarray_length != float('inf') else 0


nums = [2, 3, 1, 2, 4, 3]
target = 7
print(minSubarraySum(nums, target))
