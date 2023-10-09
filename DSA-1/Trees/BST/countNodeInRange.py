def countNodesInRange(node, B, C):
    if node:
        total = 0
        if B <= node.val <= C:
            total += 1
        total += countNodesInRange(node.left, B, C)
        total += countNodesInRange(node.right, B, C)
        return total
    return 0
