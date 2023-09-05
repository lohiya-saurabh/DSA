def nextGreater(A):
    nextGreaterToRight = [-1]*len(A)
    for i in range(len(A) - 2, -1, -1):
        j = i + 1
        while j < len(A):
            if A[j] > A[i]:
                nextGreaterToRight[i] = A[j]
                break
            j += 1
    return nextGreaterToRight


arr = [34, 35, 27, 42, 5, 28, 39, 20, 28]
print(nextGreater(arr))
