def solve(A, B):
    unique_points = {}
    for i in range(len(A)):
        unique_points[str(A[i]) + "-" + str(B[i])] = False
    count = 0
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if A[i] != A[j] and B[i] != B[j]:
                if str(A[i]) + "-" + str(B[j]) in unique_points:
                    count += 1
                if str(A[j]) + "-" + str(B[i]) in unique_points:
                    count += 1
    return count % (10**9 + 7)


A = [1, 1, 2, 2]
B = [1, 2, 1, 2]

print(solve(A, B))
