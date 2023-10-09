def solve(A, B):
    binA = list(bin(A))
    if len(binA) >= B + 2:
        if binA[-(B + 1)] == '1':
            binA[-(B + 1)] = '0'
            return int("".join(binA), 2)
    if len(binA) < B + 2:
        binA = ["0" for _ in range(B + 1 - len(binA))] + binA[2:]
    binA[-(B + 1)] = '1'
    return int("".join(binA), 2)

print(solve(89, 9))