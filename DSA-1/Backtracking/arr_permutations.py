def permute(A):
    visited = [False for _ in range(len(A))]
    return permuteHelper(A, A.copy(), 0, visited, [])


def permuteHelper(arr, ans, idx, visited, permutations):
    if idx == len(arr):
        permutations.append(ans)
        return permutations
    for i in range(len(arr)):
        if visited[i] == False:
            visited[i] = True
            ans[idx] = arr[i]
            permutations = permuteHelper(
                arr, ans.copy(), idx + 1, visited, permutations)
            visited[i] = False
    return permutations


print(permute([1, 2, 3]))
