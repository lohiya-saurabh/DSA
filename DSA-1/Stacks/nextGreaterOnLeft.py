def nextGreaterOnLeft(arr):
    stack = []
    nsl = []
    for i, ele in enumerate(arr):
        if len(stack) == 0:
            nsl.append(-1)
        else:
            while stack and arr[stack[-1]] <= ele:
                stack.pop()
            if stack:
                nsl.append(stack[-1])
            else:
                nsl.append(-1)
        stack.append(i)
    return nsl


arr = [3, 3, 4, 6, 1, 2, 9, 10, 8]
print(nextGreaterOnLeft(arr))
