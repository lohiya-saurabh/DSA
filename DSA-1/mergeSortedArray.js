var merge = function (nums1, nums2) {
  let p1 = 0
  let p2 = 0
  while (p1 < nums2.length) {
    if (nums1[p1] <= nums2[p2]) {
      p1++
    } else {
      let temp = nums2[p2]
      nums2[p2] = nums1[p1]
      nums1[p1] = temp
    }
    while (p2 < nums2.length - 1) {
      if (nums2[p2] > nums2[p2 + 1]) {
        let temp = nums2[p2]
        nums2[p2] = nums2[p2 + 1]
        nums2[p2 + 1] = temp
        p2++
      }
      else break;
    }
    p2 = 0
  }
  p1 = nums1.length - nums2.length
  p2 = 0
  while (p1 < nums1.length) {
    nums1[p1] = nums2[p2]
    p1++
    p2++
  }
  return nums1
};

console.log(merge([9, 13, 19, 0, 0, 0], [1, 8, 14]))
// console.log(merge([0], [1]))