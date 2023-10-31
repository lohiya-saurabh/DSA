def minGroupsForValidAssignment(nums):
    poolSizes = {}
    for num in nums:
        if num in poolSizes:
            poolSizes[num] += 1
        else:
            poolSizes[num] = 1
    
    poolSizes = list(poolSizes.values())
    poolSizes.sort()
    for i in range(poolSizes[0], 0, -1):
        currPoolSize = 0
        for j in range(len(poolSizes)):
            if poolSizes[j]%i < i - 1:
                break
            else:
                currPoolSize += poolSizes[j]//i + 1 if poolSizes[j]%i != 0 else 0
        if j == len(poolSizes):
            return currPoolSize

print(minGroupsForValidAssignment([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]))