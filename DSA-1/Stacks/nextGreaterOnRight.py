def nextGreaterOnRight(arr):
    stack = []
    nsr = []
    n = len(arr)
    for i in range(n - 1, -1, -1):
        if len(stack) == 0:
            nsr.append(n)
        else:
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()
            if stack:
                nsr.append(stack[-1])
            else:
                nsr.append(n)
        stack.append(i)
    return nsr[::-1]


arr = [3, 4, 6, 1, 2, 9, 10, 8, 8]
print(nextGreaterOnRight(arr))
