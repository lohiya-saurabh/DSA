import { node1 as root } from './index.js'

function isValidBST(root) {
  let cond1 = true
  let cond2 = true
  if (root) {
    if (root.left) {
      if (root.val > root.left.val) {
        cond1 = isValidBST(root.left)
      } else return false
    }
    if (root.right) {
      if (root.val < root.right.val) {
        cond1 = isValidBST(root.right)
      } else return false
    }
  }
  return cond1 && cond2
};

console.log(isValidBST(root))

