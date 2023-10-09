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
                node.val = findMin(node.right)
                node.right = deleteNodeFromBST(node.right, node.val)
    return node


def findMin(node):
    while node.left:
        node = node.left
    return node.val