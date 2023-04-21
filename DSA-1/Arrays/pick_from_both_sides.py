def pickFromBothSides(A, B):
    leftToRight = [0] * len(A)
    rightToLeft = [0] * len(A)
    if len(A):
        leftToRight[0] = A[0]
        rightToLeft[-1] = A[-1]
    for i in range(1, len(A)):
        leftToRight[i] = leftToRight[i - 1] + A[i]
    for i in range(len(A) - 2, -1, -1):
        rightToLeft[i] = rightToLeft[i + 1] + A[i]
    maxPossibleSum = float('-inf')
    for i in range(B + 1):
        leftSum = leftToRight[i - 1] if i > 0 else 0
        rightSum = rightToLeft[len(A) - B + i] if i < B else 0
        maxPossibleSum = max(maxPossibleSum, leftSum + rightSum)
    return maxPossibleSum


print(pickFromBothSides([1, 2, 3, 2, 1], 2))

# 10 3 7 5 1 9 5 8 15

# inf 10 3 3 1
