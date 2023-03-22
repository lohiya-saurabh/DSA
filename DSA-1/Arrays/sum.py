def solve(A, B):
    dictA = {}
    dictB = {}
    common = []
    for num in A:
        if num in dictA:
            dictA[num] += 1
        else:
            dictA[num] = 1
    for num in B:
        if num in dictB:
            dictB[num] += 1
        else:
            dictB[num] = 1
    for num in set(A):
        if num in dictA and num in dictB:
            common = common + [num] * min(dictA[num], dictB[num])
    return common


print(solve([1, 2, 2, 1], [2, 3, 2, 1]))
