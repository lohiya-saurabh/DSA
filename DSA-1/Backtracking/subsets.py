def subsets(A):
    ans = subsetsHelper(A, [], [], 0)
    ans.pop()
    return ans


def subsetsHelper(arr, currSubset, subsets, idx):
    if idx == len(arr):
        subsets.append(currSubset)
        return subsets
    currSubset.append(arr[idx])
    subsets = subsetsHelper(
        arr, currSubset.copy(), subsets, idx + 1)
    currSubset.pop()
    subsets = subsetsHelper(
        arr, currSubset.copy(), subsets, idx + 1)
    return subsets


print(subsets([1, 2, 3]))
