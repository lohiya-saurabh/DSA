from trees import TreeNode

def solve(A):
    calculateHeightOfTree(A)
    return DiameterOfTree(A)

def DiameterOfTree(node):
    if not node:
        return 0
    leftTreeHeight = node.left.height + 1 if node.left else 0
    rightTreeHeight = node.right.height + 1 if node.right else 0
    return max(leftTreeHeight + rightTreeHeight, DiameterOfTree(node.left), DiameterOfTree(node.right))

def calculateHeightOfTree(node):
    if not node:
        return -1
    node.height = max(calculateHeightOfTree(node.left), calculateHeightOfTree(node.right)) + 1
    return node.height



node1 = TreeNode(106)
node2 = TreeNode(480)
node3 = TreeNode(454)
node4 = TreeNode(321)
node5 = TreeNode(719)

node1.right = node2
node2.left = node3
node2.right = node4
node4.left = node5

print(solve(node1))