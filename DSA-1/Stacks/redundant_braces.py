def braces(A):
    stack = []
    operands = set(["+", "-", "*", "/"])
    for char in A:
        if char == ")":
            count = 0
            while stack[-1] != "(":
                if stack.pop() in operands:
                    count = 1
            if count == 0:
                return 1
            stack.pop()
        else:
            stack.append(char)
    return 0
