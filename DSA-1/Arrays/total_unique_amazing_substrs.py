def total_unique_amazing_substrs(A):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    totalUniqueAmazSubstrs = set()
    n = len(A)
    for i in range(n):
        if A[i] in vowels:
            for j in range(i, n):
                totalUniqueAmazSubstrs.add(A[i: j + 1])
    return len(totalUniqueAmazSubstrs)


print(total_unique_amazing_substrs("esate"))
