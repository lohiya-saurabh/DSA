def minSum(nums1, nums2):
    zeroCountNums1 = 0
    sumNums1 = 0
    for num in nums1:
        if num == 0:
            zeroCountNums1 += 1
        sumNums1 += num
    zeroCountNums2 = 0
    sumNums2 = 0
    for num in nums2:
        if num == 0:
            zeroCountNums2 += 1
        sumNums2 += num
    if zeroCountNums1 == 0 and zeroCountNums2 == 0:
        if sumNums1 != sumNums2:
            return -1
        else:
            return sumNums1
    if zeroCountNums1 > 0 and zeroCountNums2 > 0:
        return max(sumNums1 + zeroCountNums1, sumNums2 + zeroCountNums2)
    if zeroCountNums1 == 0:
        if sumNums1 >= (sumNums2 + zeroCountNums2):
            return sumNums1
        return -1
    if zeroCountNums2 == 0:
        if sumNums2 >= (sumNums1 + zeroCountNums1):
            return sumNums2
        return -1