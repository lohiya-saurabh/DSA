class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def rightView(root):
    queue = [root]
    lot = []
    right_view = []
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
    for level in lot:
        right_view.append(level[-1])
    return right_view
