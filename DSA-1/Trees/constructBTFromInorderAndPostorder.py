from trees import TreeNode


def constructBinaryTreeFromInorderAndPreorder(self, inorder, preorder):
    inorder_map = {}
    for i, num in enumerate(inorder):
        inorder_map[num] = i
    return self.constructBTHelperFromInorderAndPreorder(inorder_map, inorder, preorder, 0, len(inorder), 0, len(preorder))


def constructBTHelperFromInorderAndPreorder(inorder_map, inorder, preorder, in_start, in_end, post_start, post_end):
    if in_start == in_end or post_start == post_end:
        return
    root_val = preorder[post_start]
    root_index = inorder_map[root_val]
    root = TreeNode(root_val)
    left_tree_size = root_index - in_start
    root.left = constructBTHelperFromInorderAndPreorder(
        inorder_map, inorder, preorder, in_start, root_index, post_start + 1, post_start + left_tree_size + 1)
    root.right = constructBTHelperFromInorderAndPreorder(
        inorder_map, inorder, preorder, root_index + 1, in_end, post_start + left_tree_size + 1, post_end)
    return root


inorderTraversal = [4, 2, 5, 1, 6, 3, 7]
preorderTraversal = [4, 5, 2, 6, 7, 3, 1]
root = constructBinaryTreeFromInorderAndPreorder(
    inorderTraversal, preorderTraversal)
print(root)
