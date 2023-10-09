from trees import TreeNode

def solve(A):
    sumOfTree(A)
    return 1 if inorderTraversal(A) else 0
    

def sumOfTree(node):
    if not node:
        return 0
    node.treeSum = node.val + sumOfTree(node.left) + sumOfTree(node.right)
    return node.treeSum

def inorderTraversal(root, traversal=[]):
    if root:
        inorderTraversal(root.left, traversal)
        if 2*root.treeSum in traversal:
            return True
        traversal.append(root.treeSum)
        inorderTraversal(root.right, traversal)

    return traversal


# def equalTreePartition(root):
#     if not root:
#         return False
#     leftTreeSum = root.left.treeSum if root.left else 0
#     rightTreeSum = root.right.treeSum if root.right else 0
#     if root.treeSum == 2*leftTreeSum or root.treeSum == 2*rightTreeSum:
#         return True
#     else: 
#         return equalTreePartition(root.left) and equalTreePartition(root.right)




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