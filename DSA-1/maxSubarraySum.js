var maxSubArray = function (nums) {
  let subArraySum = []
  let overhead = 0
  for (let i = 0; i < nums.length; i++) {
    let max = Math.max(nums[i] + overhead, nums[i])
    subArraySum.push(max)
    overhead = subArraySum.slice(-1).pop()
  }
  console.log(subArraySum)
  return Math.max(...subArraySum)
};

maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])