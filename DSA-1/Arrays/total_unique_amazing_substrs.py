def total_amazing_substrs(A):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    n = len(A)
    total = 0
    for i in range(n):
        if A[i] in vowels:
            total += n - i
    return total


print(total_amazing_substrs("esate"))
