def solve(A, B):
    binA = list(bin(A))
    if len(binA) >= B + 2:
        binA[-(B + 1)] = '0'
    return int("".join(binA), 2)

print(solve(89, 9))