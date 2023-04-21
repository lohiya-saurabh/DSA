def solve(A):
    ans = []
    for i in range(len(A)):
        currArr = []
        for j in range(i, len(A)):
            currArr.append(A[j])
            ans.append(currArr.copy())
    return ans


print(solve([2, 4, 1]))
