def search(nums, target):
    return __searchHelper(0, len(nums) - 1, nums, target)


def __searchHelper(start, end, arr, target):
    while start <= end:
        middle = (start + end)//2
        if arr[middle] == target:
            return middle
        elif arr[start] <= arr[middle]:
            if arr[start] <= target and arr[middle] > target:
                end = middle - 1
            else:
                start = middle + 1
        else:
            if arr[end] >= target and arr[middle] < target:
                start = middle + 1
            else:
                end = middle - 1
    return -1


arr = [3, 5, 1]
target = 3

print(search(arr, target))
