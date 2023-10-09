def solve(A):
    if len(A) <= 2:
        return 1

    min_val = min(A)
    max_val = max(A)
    n = len(A)

    arr_map = {}
    common_difference = (max_val - min_val) / (n - 1)
    for ele in A:
        if ele in arr_map:
            arr_map[ele] += 1
        else:
            arr_map[ele] = 1
    start = min_val
    i = 0
    while i < len(A) :
        if start in arr_map:
            if arr_map[start] > 1:
                arr_map[start] -= 1
            else:
                del arr_map[start]
        else:
            return 0
        start += common_difference
        i += 1
    return 1

print(solve([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))