class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def levelOrderTraversal(root):
    queue = [root]
    lot = []
    if not root:
        return
    while len(queue) > 0:
        curr_len = len(queue)
        curr_level = []
        while curr_len > 0:
            node = queue.pop(0)
            curr_level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            curr_len -= 1
        lot.append(curr_level)
    return lot
