
def merge(A, B):
    s1, s2, e1, e2 = len(B), 0, len(A) + len(B), len(B)
    for _ in B:
        A.insert(0, 0)
    i = 0
    while s1 < e1 and s2 < e2:
        if A[s1] <= B[s2]:
            A[i] = A[s1]
            s1 += 1
        else:
            A[i] = B[s2]
            s2 += 1
        i += 1
    while s1 < e1:
        A[i] = A[s1]
        s1 += 1
        i += 1
    while s2 < e2:
        A[i] = B[s2]
        s2 += 1
        i += 1


A = [1, 5, 8]
B = [6, 9]
print(merge(A, B))
