def longestSubarrayZeroSum(A):
    n = len(A)
    prefix_sum = [0]*n
    prefix = 0
    for i, num in enumerate(A):
        prefix += num
        prefix_sum[i] += prefix
    prefix_sum_map = {}
    max_subarray_length = 0
    for i, num in enumerate(prefix_sum):
        if num in prefix_sum_map:
            max_subarray_length = max(
                max_subarray_length, i - prefix_sum_map[num])
        else:
            prefix_sum_map[num] = i
        if num == 0:
            max_subarray_length = max(max_subarray_length, i + 1)
    return max_subarray_length
