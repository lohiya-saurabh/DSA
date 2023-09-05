def searchInsert(nums, target):
    return __searchInsertPositionHelper(nums, 0, len(nums) - 1, target)


def __searchInsertPositionHelper(arr, left, right, target):
    while left <= right:
        middle = (left + right)//2
        if arr[middle] > target:
            right = middle - 1
        elif arr[middle] < target:
            left = middle + 1
        else:
            return middle
    return left


arr = [1, 3, 5, 7]
target = 5

print(searchInsert(arr, 5))
