def maxSubarray(A, B, C):
    subarraySums = []
    for i in range(A):
        currSum = 0
        for j in range(i, A):
            currSum += C[j]
            subarraySums.append(currSum)
    maxSum = 0
    print(subarraySums)
    for i in range(len(subarraySums)):
        if subarraySums[i] > maxSum and subarraySums[i] <= B:
            maxSum = subarraySums[i]
    return maxSum


print(maxSubarray(1, 75,  [5]))
