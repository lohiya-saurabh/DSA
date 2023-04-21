def targetSum(arr, k):
    dict1 = {}
    ans = []
    for num in arr:
        dict1[num] = True
    for i in range(len(arr)):
        if k - arr[i] in dict1 and dict1[k - arr[i]]:
            ans.append([arr[i], k - arr[i]])
            # If we don't want duplicate pairs
            dict1[arr[i]] = False
            dict1[k - arr[i]] = False
    return ans


print(targetSum([8, 9, 1, 5, -5, 6, 3, 5, 5, 4], 9))
