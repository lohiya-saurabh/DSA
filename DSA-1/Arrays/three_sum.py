def threeSum(nums):
    i = 0
    k = len(nums) - 1
    nums.sort()
    ans = []
    while i < k:
        j = i + 1
        while j < k:
            tmp = nums[i] + nums[j] + nums[k]
            if tmp == 0 and not ([nums[i], nums[j], nums[k]] in ans):
                ans.append([nums[i], nums[j], nums[k]])
            if tmp == 0:
                j += 1
                k -= 1
            elif tmp < 0:
                j += 1
            elif tmp > 0:
                k -= 1
        i += 1
    return ans


def threeSumClosest(A, B):
    A.sort()
    i, k = 0, len(A) - 1
    closest = float('inf')
    while i < k:
        start = i + 1
        end = k
        curr_sum = float('inf')
        while start < end:
            mid = (start + end)//2
            curr_sum = A[i] + A[mid] + A[k]
            if abs(curr_sum - B) == 0:
                return curr_sum
            if curr_sum < B:
                start = mid + 1
            else:
                end = mid
            if abs(curr_sum - B) < abs(closest - B):
                closest = curr_sum
        if curr_sum > B:
            k -= 1
        else:
            i += 1
    return closest


arr = [-8, -6, -5, 3, 4, 10]
B = 3

print(threeSumClosest(arr, B))
