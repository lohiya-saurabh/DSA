
def isBalanced(root):
    _, isTreeHeightBalanced = checkHeightAndBalance(root)
    return 1 if isTreeHeightBalanced else 0


def checkHeightAndBalance(node):
    if not node:
        return 0, True

    leftTreeHeight, leftTreeBalance = checkHeightAndBalance(node.left)
    rightTreeHeight, rightTreeBalance = checkHeightAndBalance(node.right)

    currentHeight = 1 + max(leftTreeHeight, rightTreeHeight)
    currentNodeBalance = abs(leftTreeHeight - rightTreeHeight) <= 1

    isTreeBalanced = leftTreeBalance and rightTreeBalance and currentNodeBalance

    return currentHeight, isTreeBalanced
