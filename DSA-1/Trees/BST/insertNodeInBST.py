from trees import TreeNode

def insertNodeInBST(tree, node):
    if not tree:
        return node
    if tree.val < node.val:
        tree.right = insertNodeInBST(tree.right, node)
    else:
        tree.left = insertNodeInBST(tree.left, node)
    return tree 
node1 = TreeNode(106)
node2 = TreeNode(480)
node3 = TreeNode(102)

node1.right = node2
node1.left = node3

node = insertNodeInBST(node1, TreeNode(454))
print(node)