class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    # Calculate Height of Binary Tree
    def calculateHeight(self):
        if not self:
            return 0
        leftHeight = 0
        rightHeight = 0
        if self.left:
            leftHeight = self.left.calculateHeight()
        if self.right:
            rightHeight = self.right.calculateHeight()
        return 1 + max(leftHeight, rightHeight)

    # Construct Binary Tree From Preorder and Inorder Tree
    def constructTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        m = inorder.index(preorder[0])
        root.left = self.constructTree(preorder[1:m + 1], inorder[:m])
        root.right = self.constructTree(preorder[m + 1:], inorder[m + 1:])
        return root
    # Construct BT from preorder and inorder Traversal arrays

    def constructBTFromInorderAndPreorder(self, preorder, inorder):
        inorder_map = {inorder[i]: i for i in range(len(inorder))}
        print(inorder_map)
        return self.__constructBTHelper(inorder_map, inorder, preorder, 0, len(inorder), 0, len(preorder))

    def __constructBTHelper(self, inorder_map, inorder, preorder, in_start, in_end, pre_start, pre_end):
        if pre_start == pre_end or in_start == in_end:
            return None
        root_val = preorder[pre_start]
        root_index = inorder_map[root_val]
        root = TreeNode(root_val)
        leftyTreeSize = root_index - in_start
        root.left = self.__constructBTHelper(
            inorder_map, inorder, preorder, in_start, root_index, pre_start + 1, pre_start + leftyTreeSize + 1)
        root.right = self.__constructBTHelper(
            inorder_map, inorder, preorder, root_index + 1, in_end, pre_start + leftyTreeSize + 1, pre_end)
        return root

    def pathSum(self, root, currentSum=0, ans=[]):
        if root:
            if not root.left and not root.right:
                ans.append(currentSum + root.val)
            else:
                self.pathSum(root.left, currentSum+root.val, ans)
                self.pathSum(root.right, currentSum+root.val, ans)
        return ans

    def pathSumArrays(self, root, targetSum=0, currentSum=0, currArr=[], ans={}):
        if root:
            if not root.left and not root.right:
                if currentSum + root.val in ans:
                    ans[currentSum +
                        root.val] = ans[currentSum + root.val].append(currArr+[root.val])
                else:
                    ans[currentSum+root.val] = [currArr + [root.val]]
            else:
                self.pathSumArrays(root.left, targetSum,
                                   currentSum + root.val, currArr + [root.val], ans)
                self.pathSumArrays(root.right, targetSum,
                                   currentSum + root.val, currArr + [root.val], ans)
        return ans

    def maxPathSum(self, node):
        self.max_sum = float('-inf')

        def maxPathSumHelper(node):
            if not node:
                return 0
            left_sum = maxPathSumHelper(node.left)
            right_sum = maxPathSumHelper(node.right)
            node.max_path_sum = max(
                node.val, node.val + left_sum, node.val + right_sum)
            max_sum_through_node = max(
                node.max_path_sum, node.val + left_sum + right_sum)
            self.max_sum = max(self.max_sum, max_sum_through_node)
            return node.max_path_sum

        maxPathSumHelper(node)

        return self.max_sum

    # Zigza g Level Order Traversal
    def levelOrderTraversal(self, root):
        if not root:
            return []
        traversal = []
        currentLevel = [root]
        dirct = True
        while currentLevel:
            nextLevel = []
            currentLevelLength = len(currentLevel)
            while currentLevelLength:
                node = currentLevel.pop(0)
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
                currentLevel.append(node.val)
                currentLevelLength -= 1
            if dirct:
                traversal.append(currentLevel)
            else:
                traversal.append(currentLevel[::-1])
            currentLevel = nextLevel
            dirct = not dirct
        return traversal

    def timeTakenToBurnWholeTree(self, A, B):
        parents = {}
        queue = [A]
        timeTaken = 0
        if not A:
            return 0
        while queue:
            node = queue.pop()
            if node.left:
                queue.append(node.left)
                parents[node.left.val] = node
            if node.right:
                queue.append(node.right)
                parents[node.right.val] = node

        burned = set()
        node = None
        if B == A.val:
            node = A
        else:
            node_parent = parents[B]
            if node_parent.left.val == B:
                node = node_parent.left
            elif node_parent.right.val == B:
                node = node_parent.right
        queue = [node]
        while queue:
            queueLen = len(queue)
            while queueLen:
                node = queue.pop(0)
                burned.add(node.val)
                if node.left and node.left.val not in burned:
                    queue.append(node.left)
                if node.right and node.right.val not in burned:
                    queue.append(node.right)
                if node.val in parents and parents[node.val].val not in burned:
                    queue.append(parents[node.val])
                queueLen -= 1
            timeTaken += 1
        return timeTaken - 1

    def getMinimumDifference(self, root):
        min_diff = float('inf')
        inorder_traversal = self.inorderTraversal(root)
        for i in range(1, len(inorder_traversal)):
            min_diff = min(
                min_diff, inorder_traversal[i] - inorder_traversal[i - 1])
        return min_diff

    def inorderTraversal(self, root, traversal=[]):
        if root:
            self.inorderTraversal(root.left, traversal)
            traversal.append(root.val)
            self.inorderTraversal(root.right, traversal)

        return traversal

    def isSymmetric(self, root):
        if root:
            return self.isSymmetricHelper(root.left, root.right)
        return True

    def isSymmetricHelper(self, node1, node2):
        if node1 and node2:
            if node1.val == node2.val:
                return self.isSymmetricHelper(node1.left, node2.right) and self.isSymmetricHelper(node1.right, node2.left)
            return False
        elif (node1 and not node2) or (not node1 and node2):
            return False
        return True

    def constructBinaryTreeFromInorderAndPostorder(self, inorder, postorder):
        inorder_map = {}
        for i, num in enumerate(inorder):
            inorder_map[num] = i
        return self.__constructBTHelperFromInorderAndPreorder(inorder_map, inorder, postorder, 0, len(inorder), 0, len(postorder))

    def __constructBTHelperFromInorderAndPostorder(self, inorder_map, inorder, postorder, in_start, in_end, post_start, post_end):
        if in_start == in_end or post_start == post_end:
            return
        root_val = postorder[post_start]
        root_index = inorder_map[root_val]
        root = TreeNode(root_val)
        left_tree_size = root_index - in_start
        root.left = self.__constructBTHelperFromInorderAndPostorder(
            inorder_map, inorder, postorder, in_start, root_index, post_start + 1, post_start + left_tree_size + 1)
        root.right = self.__constructBTHelperFromInorderAndPostorder(
            inorder_map, inorder, postorder, root_index + 1, in_end, post_start + left_tree_size + 1, post_end)
        return root

    def hasPathSum(self, root, targetSum):
        return self.__hasPathSumHelper(root, 0, targetSum)

    def __hasPathSumHelper(self, node, trailing_sum, target):
        if node:
            left, right = False, False
            if node.left:
                left = self.__hasPathSumHelper(
                    node.left, trailing_sum + node.val, target)
            if node.right:
                right = self.__hasPathSumHelper(
                    node.right, trailing_sum + node.val, target)
            if not node.left and not node.right:
                return trailing_sum + node.val == target
            return left or right
        return False

    def sumNumbers(self, root):
        total_numbers_sum = 0
        return self.__sumNumbersHelper(root, 0, total_numbers_sum)

    def __sumNumbersHelper(self, node, trailing_number, total_numbers_sum):
        if node:
            if node.left:
                total_numbers_sum = self.__sumNumbersHelper(
                    node.left, trailing_number*10 + node.val, total_numbers_sum)
            if node.right:
                total_numbers_sum = self.__sumNumbersHelper(
                    node.right, trailing_number*10 + node.val, total_numbers_sum)
            if not node.left and not node.right:
                total_numbers_sum += trailing_number*10 + node.val
        return total_numbers_sum

    def countNodes(self, root) -> int:
        total_nodes = 0
        return self.__countNodesHelper(root, 0, total_nodes)

    def __countNodesHelper(self, node, trailing_node_count, total_nodes):
        if node:
            left_count, right_count = 0, 0
            if node.left:
                left_count = self.__countNodesHelper(
                    node.left, trailing_node_count + 1, total_nodes)
            if node.right:
                right_count = self.__countNodesHelper(
                    node.right, trailing_node_count + 1, total_nodes)
            return left_count + right_count + 1
        return total_nodes

    def flattenTree(self, node):

        # Handle the null scenario
        if not node:
            return None

        # For a leaf node, we simply return the
        # node as is.
        if not node.left and not node.right:
            return node

        # Recursively flatten the left subtree
        leftTail = self.flattenTree(node.left)

        # Recursively flatten the right subtree
        rightTail = self.flattenTree(node.right)

        # If there was a left subtree, we shuffle the connections
        # around so that there is nothing on the left side
        # anymore.
        if leftTail:
            leftTail.right = node.right
            node.right = node.left
            node.left = None

        # We need to return the "rightmost" node after we are
        # done wiring the new connections.
        return rightTail if rightTail else leftTail

    def flatten(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        self.flattenTree(root)


preorder = [1, 2, 4, 5, 6, 3, 8]
inorder = [4, 2, 6, 5, 1, 3, 8]

n = TreeNode(2)
node1 = TreeNode(1)
node2 = TreeNode(0)
node3 = TreeNode(48)
node4 = TreeNode(12)
node5 = TreeNode(49)

node1.left = node2
node1.right = node3
node3.left = node4
node3.right = node5


# print(node1.getMinimumDifference(node1))

# root = node1.constructBinaryTreeFromInorderAndPreorder(inorder, preorder)

# print(root.levelOrderTraversal(root))
