def solve(A):
    rowIndex = 0
    maxOnes = 0
    for i, arr in enumerate(A):
        onesCount = binarySearch(arr)
        if onesCount > maxOnes:
            rowIndex = i
    return rowIndex


def binarySearch(nums):
    return binarySearchHelper(nums, 0, len(nums) - 1)

def binarySearchHelper(arr, left, right):
    while left <= right:
        middle = (left + right)//2
        if middle < len(arr) - 1:
            if arr[middle] == 0 and arr[middle + 1] == 1:
                return len(arr) - middle
            elif arr[middle] == 1:
                right = middle - 1
            else:
                left = middle + 1
        if middle == 0:
            if arr[middle] == 1:
                return len(arr)
            else:
                left += 1
    return 0

matrix = [[0, 0, 0, 1], [0, 1, 1, 1], [0, 0, 1, 1]]
print(solve(matrix))