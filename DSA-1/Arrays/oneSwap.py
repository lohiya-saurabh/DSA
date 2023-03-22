class Solution:
    def sortColors(self, nums) -> None:
        low = 0
        mid = 0
        high = len(nums) - 1
        self.nums = nums

        while mid <= high:
            if nums[mid] == 0:
                self.swap(low, mid)
                low += 1
                mid += 1
            elif nums[mid] == 2:
                self.swap(mid, high)
                high -= 1
            else:
                mid += 1
        return nums

    def swap(self, i, j):
        [self.nums[i], self.nums[j]] = [self.nums[j], self.nums[i]]
