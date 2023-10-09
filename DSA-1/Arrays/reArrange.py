def arrange(A):
    i = 0
    while i < len(A):
        while i != A[i]:
            ele = A[i]
            A[i], A[ele] = A[ele], A[i]
        i += 1
    return A


print(arrange([4, 0, 2, 1, 3]))
