# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def solve(A, B):
    return deleteNodeFromBST(A, B)


def deleteNodeFromBST(node, key):
    if node:
        if node.val < key:
            node.right = deleteNodeFromBST(node.right, key)
        elif node.val > key:
            node.left = deleteNodeFromBST(node.left, key)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                node.val = findMax(node.left)
                node.left = deleteNodeFromBST(node.left, node.val)
    return node


def findMax(node):
    while node.right:
        node = node.right
    return node.val


def inorderTraversal(root, traversal=[]):
    if root:
        inorderTraversal(root.left, traversal)
        traversal.append(root.val)
        inorderTraversal(root.right, traversal)

    return traversal
# Create a test case for the above function


# Test case 1
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left.left = TreeNode(1)
root.right.right = TreeNode(7)
inorder = solve(root, 3)

print(inorderTraversal(inorder))
