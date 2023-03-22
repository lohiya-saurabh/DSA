var hasPathSum = function (root, targetSum) {
  let sums = []
  function branchSums(node, sum, sums) {
    if (node) {
      if (!node.left && !node.right) {
        sums.push(sum + node.val)
      } if (node.left) {
        sums = branchSums(node.left, sum + node.val, sums)
      } if (node.right) {
        sums = branchSums(node.right, sum + node.val, sums)
      }
    }
    return sums
  }
  sums = branchSums(root, 0, sums)
  return sums.includes(targetSum)
};

console.log(hasPathSum(node1, 12))