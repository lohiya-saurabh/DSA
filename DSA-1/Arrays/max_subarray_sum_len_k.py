def max_subarray_sum_len_k(arr, k):
    n = len(arr)
    if k >= n:
        return sum(arr)
    max_subarray_sum = 0
    for i in range(k):
        max_subarray_sum += arr[i]
    current_sum = max_subarray_sum
    for i in range(k, n):
        current_sum += arr[i] - arr[i - k]
        max_subarray_sum = max(current_sum, max_subarray_sum)
    return max_subarray_sum


print(max_subarray_sum_len_k([8, -3, 2, 6, 1, 0, -4, 9, 13, -12], 3))
