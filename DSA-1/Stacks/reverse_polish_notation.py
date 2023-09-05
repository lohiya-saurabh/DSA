
def evalRPN(A):
    n = len(A)
    operators = set(["+", "/", "-", "*"])
    stack = []
    i = 0
    while i < n:
        if not A[i] in operators:
            stack.append(int(A[i]))
        else:
            b = stack.pop()
            a = stack.pop()
            stack.append(evalOperators(a, b, A[i]))
        i += 1

    return stack.pop()


def evalOperators(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if a < 0 or b < 0:
            return -1 * (abs(a) // abs(b))
        return a // b


print(evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
              ))
