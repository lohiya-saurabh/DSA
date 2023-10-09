from trees import TreeNode


def distanceBetweenNodes(A, B, C):
    parents = {}
    parents = childParentMapping(A, parents)
    if B in parents:
        if parents[B].left and parents[B].left.val == B:
            curr_node = parents[B].left
        else:
            curr_node = parents[B].right
    else:
        curr_node = A

    neighbours = [curr_node]
    next_queue = []
    distance = 0
    visited = set()
    while neighbours:
        current = neighbours.pop(0)
        visited.add(current.val)
        if current.val == C:
            return distance
        if current.val in parents and parents[current.val] not in visited:
            next_queue.append(parents[current.val])
        if current.right and current.right.val not in visited:
            next_queue.append(current.right)
        if current.left and current.left.val not in visited:
            next_queue.append(current.left)
        if not neighbours:
            neighbours = next_queue
            next_queue = []
            distance += 1
    return distance


def childParentMapping(root, parents):
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node.left:
            parents[node.left.val] = node
            queue.append(node.left)
        if node.right:
            parents[node.right.val] = node
            queue.append(node.right)
    return parents


root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(1)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

print(distanceBetweenNodes(root, 4, 9))
