from Trees.trees import TreeNode


def isBST(root, min_val, max_val):

    if root is None:
        return True

    if not (min_val < root.val < max_val):
        return False

    return isBST(root.left, min_val, root.val) and isBST(root.right, root.val, max_val)


root = TreeNode(5)
print(isBST(root, float('-inf'), float('inf')))
