def findOccurences(A):
    dict1 = {}
    for num in A:
        if num in dict1:
            dict1[num] += 1
        else:
            dict1[num] = 1
    ans = []
    A = sorted(list(set(A)))
    for num in A:
        ans.append(dict1[num])
    return ans


print(findOccurences([56, 35, 25, 32, 41, 50, 7,
      52, 34, 41, 72, 12, 93, 50, 19, 94, 13, 19]))
