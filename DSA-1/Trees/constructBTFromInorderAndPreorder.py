from trees import TreeNode


def constructBinaryTreeFromInorderAndPostorder(inorder, postorder):
    inorder_map = {}
    for i, num in enumerate(inorder):
        inorder_map[num] = i
    return constructBTHelperFromInorderAndPostorder(inorder_map, inorder, postorder, 0, len(inorder), len(postorder) - 1, -1)


def constructBTHelperFromInorderAndPostorder(inorder_map, inorder, postorder, in_start, in_end, post_start, post_end):
    if in_start == in_end or post_start == post_end:
        return
    root_val = postorder[post_start]
    root_index = inorder_map[root_val]
    root = TreeNode(root_val)
    right_tree_size = in_end - root_index - 1
    root.right = constructBTHelperFromInorderAndPostorder(
        inorder_map, inorder, postorder, root_index + 1, in_end, post_start - 1, post_start - (right_tree_size + 1))
    root.left = constructBTHelperFromInorderAndPostorder(
        inorder_map, inorder, postorder, in_start, root_index, post_start - (right_tree_size + 1), post_end)
    return root


inorderTraversal = [4, 2, 5, 1, 6, 3, 7]
postorderTraversal = [4, 5, 2, 6, 7, 3, 1]
root = constructBinaryTreeFromInorderAndPostorder(
    inorderTraversal, postorderTraversal)
print(root)
