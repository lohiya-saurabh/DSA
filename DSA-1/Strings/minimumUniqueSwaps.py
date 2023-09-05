def solve(A, B):
    unique_chars = set()
    dupl_chars = set()
    for char in A:
        if char in unique_chars:
            unique_chars.remove(char)
        if char not in dupl_chars:
            unique_chars.add(char)
        dupl_chars.add(char)
    min_dist_chars = len(unique_chars) - B
    print(unique_chars)
    return min_dist_chars if min_dist_chars >= 0 else 0


print(solve("umeaylnlfd", 1))
