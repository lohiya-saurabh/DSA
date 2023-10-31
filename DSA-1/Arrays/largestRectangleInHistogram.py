def largestRectangleInHistogram(arr):
    leftheight = [0] * len(arr)
    rightheight = [0] * len(arr)
    stack = []
    maxRectanglrArea = 0
    for i in range(len(arr)):
        if len(stack) != 0:
            while len(stack) != 0 and arr[stack[-1]] >= arr[i]:
                stack.pop()
        if len(stack) == 0:
            leftheight[i] = -1
        else:
            leftheight[i] = stack[-1]
        stack.append(i)
    stack = []
    for i in range(len(arr) - 1, -1, -1):
        if len(stack) != 0:
            while len(stack) != 0 and arr[stack[-1]] >= arr[i]:
                stack.pop()
        if len(stack) == 0:
            rightheight[i] = len(arr)
        else:
            rightheight[i] = stack[-1]
        stack.append(i)

    for i in range(len(arr)):
        maxRectanglrArea = max(
            maxRectanglrArea, arr[i] * (rightheight[i] - leftheight[i] - 1))
    return maxRectanglrArea


print(largestRectangleInHistogram([2, 1, 5, 6, 2, 3]))
