def cycleDetection(A, B):
    def dfs(node):
        visited.add(node)
        tmp_stack.add(node)
        for child in childrens.get(node, []):
            if child in tmp_stack:
                return 1
            elif dfs(child):
                return 1
        tmp_stack.remove(node)
        return 0
    childrens = {}
    for i in range(len(B)):
        if B[i][0] in childrens:
            childrens[B[i][0]].append(B[i][1])
        else:
            childrens[B[i][0]] = [B[i][1]]
    visited = set()
    tmp_stack = set()
    for node in range(1, A + 1):
        if node not in visited:
            if dfs(node):
                return 1
    return 0



print(cycleDetection(5, [[1, 2], [1, 3], [2, 3], [1, 4], [4, 5]]))