def specialIndex(A):
    sumOfSubarraysFromFront = []
    evenIndexArrSum = 0
    oddIndexArrSum = 0
    array_has_odd_len = False
    count = 0
    for i, val in enumerate(A):
        if not array_has_odd_len:
            evenIndexArrSum += A[i - 1] if i > 0 else 0
        else:
            oddIndexArrSum += A[i - 1]
        array_has_odd_len = not array_has_odd_len
        sumOfSubarraysFromFront.append([evenIndexArrSum, oddIndexArrSum])
    
    sumOfSubarraysFromBack = []
    evenIndexArrSum = 0
    oddIndexArrSum = 0
    array_has_odd_len = False
    for i in range(len(A) - 1, -1, -1):
        if not array_has_odd_len:
            evenIndexArrSum += A[i + 1] if i < len(A) - 1 else 0
        else:
            oddIndexArrSum += A[i + 1]
        array_has_odd_len = not array_has_odd_len
        sumOfSubarraysFromBack.append([evenIndexArrSum, oddIndexArrSum])
    sumOfSubarraysFromBack = sumOfSubarraysFromBack[::-1]
    for i in range(len(A)):
        if sumOfSubarraysFromFront[i][0] + sumOfSubarraysFromBack[i][1] == sumOfSubarraysFromFront[i][1] + sumOfSubarraysFromBack[i][0]:
            count += 1
    return count
          
print(specialIndex([1, 1, 1]))