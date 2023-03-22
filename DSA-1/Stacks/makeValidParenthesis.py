def makeValidParethesis(parenth):
    lis = list(parenth)
    newLis = []
    stack = []
    for ele in lis:
        if ele == '(':
            stack.append(ele)
            newLis.append(ele)
        elif ele == ')' and len(stack) > 0:
            stack.pop()
            newLis.append(ele)
        elif ele != ')':
            newLis.append(ele)
    if len(stack) == 0:
        return "".join(newLis)
    stack = []
    lis = newLis
    newLis = []
    for ele in lis[::-1]:
        if ele == ')':
            stack.append(ele)
            newLis.append(ele)
        elif ele == '(' and len(stack) > 0:
            stack.pop()
            newLis.append(ele)
        elif ele != '(':
            newLis.append(ele)
    return "".join(newLis[::-1])


print(makeValidParethesis('aa()(()))('))
