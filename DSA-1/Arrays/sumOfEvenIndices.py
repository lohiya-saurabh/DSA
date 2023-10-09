def solve(A, B):
    sumOfEvenIndices = [0]
    evenIndicesSum = 0
    subarrayHasOddLen = False
    for i, val in enumerate(A):
        if i&1 == 0:
            evenIndicesSum += val
        sumOfEvenIndices.append(evenIndicesSum)
    res = []
    for query in B:
        res.append(sumOfEvenIndices[query[1] + 1] - sumOfEvenIndices[query[0]])
    return res


print(solve([16,3,3,6,7,8,17,13,7], [[2,6],[4,7],[6,7]]))