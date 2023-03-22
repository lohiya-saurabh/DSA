class Solution:
    def majorityElement(self, nums) -> int:
        ele = nums[0]
        count = 0
        for num in nums:
            if num == ele:
                count += 1
            else:
                if count == 0:
                    ele = num
                    count += 1
                else:
                    count -= 1
        return ele
