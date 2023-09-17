def inorderTraversal(root, traversal=[]):
    if root:
        inorderTraversal(root.left, traversal)
        traversal.append(root.val)
        inorderTraversal(root.right, traversal)

    return traversal
