def solve(A, B):
    countOfGoofSubarrays = 0
    subarr_sum = 0
    for window_end, val in enumerate(A):
        window_start = 0
        curr_subarr_len = window_end - window_start + 1
        subarr_has_odd_len = curr_subarr_len&1 == 1
        subarr_sum += val
        curr_subarr_sum = subarr_sum
        while window_start <= window_end:
            curr_subarr_sum -= (A[window_start - 1] if window_start > 0 else 0)    
            if not subarr_has_odd_len and curr_subarr_sum < B:
                countOfGoofSubarrays += 1
            elif subarr_has_odd_len and curr_subarr_sum > B:
                countOfGoofSubarrays += 1
            subarr_has_odd_len = not subarr_has_odd_len
            window_start += 1
    return countOfGoofSubarrays


print(solve([1, 2, 3, 4, 5], 4))