def makeEqualElementsOfArray(A, B):
    ans = set([A[0] + B, A[0] - B, A[0]])
    for ele in A[1:]:
        newSet = set([ele + B, ele - B, ele])
        ans = ans.intersection(newSet)
    if len(ans) > 0:
        return 1
    return 0


print(makeEqualElementsOfArray([3, 2, 1, 2, 1, 3, 2], 2))
