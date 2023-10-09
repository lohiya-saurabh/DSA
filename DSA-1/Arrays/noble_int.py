def nobleInt(A):
    A.sort()
    for i, ele in enumerate(A):
        if ele == len(A) - (i + 1):
            return 1
    return -1

print(nobleInt([2,3,-1, 4,4]))