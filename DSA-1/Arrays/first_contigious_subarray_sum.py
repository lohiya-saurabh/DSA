def firstContiguousSubarraySum(A, B):
    n = len(A)

    left, right, currentSum = 0, 0, 0

    while left < n and right < n:

        if currentSum < B:
            currentSum += A[right]
            right += 1

        if currentSum > B:
            currentSum -= A[left]
            left += 1

        if currentSum == B:
            return (A[left:right])
    return [-1]


arr = [5, 10, 20, 100, 105]
target = 225

print(firstContiguousSubarraySum(arr, target))
