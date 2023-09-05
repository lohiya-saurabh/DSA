from trees import TreeNode


def topViewTraversal(A):
    horizontal_node_posn = levelOrderTraversal(A)
    horizontal_posn = sorted(horizontal_node_posn.keys())
    res = []
    for i in horizontal_posn:
        res.append(horizontal_node_posn[i][0])
    return res


def levelOrderTraversal(root):
    childrens = []
    current_posn = 0
    queue = [[root, current_posn]]
    if not root:
        return []
    horizontal_node_posn = dict()
    while queue:
        node, current_posn = queue.pop(0)
        if current_posn in horizontal_node_posn:
            horizontal_node_posn[current_posn].append(node.val)
        else:
            horizontal_node_posn[current_posn] = [node.val]
        if node.left:
            childrens.append([node.left, current_posn - 1])
        if node.right:
            childrens.append([node.right, current_posn + 1])
        if not queue:
            queue = childrens
            childrens = []
    return horizontal_node_posn


node1 = TreeNode(1)
node2 = TreeNode(0)
node3 = TreeNode(48)
node4 = TreeNode(12)
node5 = TreeNode(49)

node1.left = node2
node1.right = node3
node3.left = node4
node3.right = node5

print(topViewTraversal(node1))
