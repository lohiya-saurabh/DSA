def solve(A, B):
    x = A
    i = 0
    while B:
        if x & 1 == 1:
            A ^= 1 << i
        x >>= 1
        B -= 1
        i += 1
    return A


print(solve(3, 2))
