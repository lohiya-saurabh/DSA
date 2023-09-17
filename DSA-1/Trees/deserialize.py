from trees import TreeNode


def solve(A):
    if not A:
        return None
    nodes = {}
    root = TreeNode(A[0])
    nodes[0] = root
    i = 0
    reducedNodeDistance = 0
    while i < len(A):
        if A[i] != -1:
            node = nodes[i]
            leftChildIndex = 2*i + 1 - reducedNodeDistance
            rightChildIndex = 2*i + 2 - reducedNodeDistance
            if A[leftChildIndex] != -1:
                leftNode = TreeNode(A[leftChildIndex])
                node.left = leftNode
                nodes[leftChildIndex] = leftNode
            if A[rightChildIndex] != -1:
                rightNode = TreeNode(A[rightChildIndex])
                node.right = rightNode
                nodes[rightChildIndex] = rightNode
        else:
            reducedNodeDistance += 2
        i += 1
    return nodes[0]


print(solve([1, 2, 3, -1, -1, 4, 5, 9, -1, 6, 7, -1, -
      1, 8, 11, -1, 12, 10, -1, -1, -1, -1, -1, -1, -1]))
