def solve(A):
    maxA = max(A)
    count = 0
    for num in A:
        if num < maxA:
            count += 1
    return count


print(solve([3, 5, 3, 2, 9, 3, 10, 10, 10, 3]))
