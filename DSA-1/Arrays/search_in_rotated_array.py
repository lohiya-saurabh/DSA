def search(A, B):
    l, r = 0, len(A) - 1
    while l <= r:
        m = (l + r)//2
        if A[m] == B:
            return m
        elif A[m] < B:
            if A[m] < B and B <= A[r]:
                l = m + 1
        else:
            if A[l] <= B and A[m] > B:
                r = m - 1
            else:
                l = m + 1
    return -1


print(search([101, 103, 106, 109, 158, 164, 182, 187,
      202, 205, 2, 3, 32, 57, 69, 74, 81, 99, 100], 202))
