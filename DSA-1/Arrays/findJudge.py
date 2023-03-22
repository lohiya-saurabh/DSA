def findJudge(n, trust):
    if n == 1:
        return 1
    if not trust:
        return -1
    dict1 = {}
    for trs in trust:
        if trs[1] in dict1:
            dict1[trs[1]].append(trs[0])
        else:
            dict1[trs[1]] = [trs[0]]
    flag = 0
    ans = 0
    for key, val in dict1.items():
        if len(val) == n - 1:
            if flag == 0:
                flag = 1
                ans = key
            else:
                return -1
    if flag == 1:
        for trs in trust:
            if ans == trs[0]:
                return -1
        return ans
    return -1


print(findJudge(5, [[1, 2], [3, 2], [1, 3], [4, 5], [5, 2], [3, 1], [
      5, 4], [2, 1], [3, 4], [5, 1], [2, 5], [4, 1], [2, 4], [3, 5]]))
