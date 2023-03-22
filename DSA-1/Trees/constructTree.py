class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    # Construct Binary Tree From Preorder and Inorder Tree
    def constructTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        m = inorder.index(preorder[0])
        root.left = self.constructTree(preorder[1:m + 1], inorder[:m])
        root.right = self.constructTree(preorder[m + 1:], inorder[m + 1:])
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
    # Zigzag Level Order Traversal

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


node = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(3)
node.left = node1
node.right = node2
node.pathSumArrays(node, 4, 0, [], {})
