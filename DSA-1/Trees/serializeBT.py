
def serilizeBinaryTree(A):
    if not A:
        return []
    res = [A.val]
    queue = [A]
    next_level = []
    next_queue = []
    while queue:
        node = queue.pop(0)
        if node.left:
            next_queue.append(node.left)
            next_level.append(node.left.val)
        else:
            next_level.append(-1)
        if node.right:
            next_queue.append(node.right)
            next_level.append(node.right.val)
        else:
            next_level.append(-1)
        if not queue:
            queue = next_queue
            res = res + next_level
            next_level = []
            next_queue = []
    return res
