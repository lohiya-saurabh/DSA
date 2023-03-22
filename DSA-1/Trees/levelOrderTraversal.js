import { node1 as root } from './index.js'

function levelOrderTraversal(root) {
  let traversal = []
  let currentLevel = [root];

  while (currentLevel.length) {
    let currentLevelLength = currentLevel.length
    let nodes = []
    while (currentLevelLength) {
      let node = currentLevel.shift()
      nodes.push(node.val)
      if (node.left) currentLevel.push(node.left)
      if (node.right) currentLevel.push(node.right)
      currentLevelLength--;
    }
    traversal.push(nodes)
    nodes = []
  }
  return traversal;
}

console.log(levelOrderTraversal(root))
