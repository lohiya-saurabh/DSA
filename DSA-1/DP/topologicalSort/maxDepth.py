def solve(A, B, C, D, E, F):
    graph = {}
    for i in range(len(B)):
        if B[i] in graph:
            graph[B[i]].append(C[i])
        else:
            graph[B[i]] = [C[i]]
        if C[i] in graph:
            graph[C[i]].append(B[i])
        else:
            graph[C[i]] = [B[i]]
    queue = [1]
    visited = set()
    i = 0
    levels = {}
    level = 0
    levels[level] = []
    curr = []
    while i != len(queue):
        node = queue[i]
        i += 1
        levels[level].append(D[node - 1])
        visited.add(node)
        for child in graph[node]:
            if child in visited:
                continue
            curr.append(child)
        if i == len(queue):
            for n in curr:
                queue.append(n)
            curr = []
            level += 1
            levels[level] = []
    ans = []
    maxDepth = level
    for i in range(len(E)):
        minValue = float('inf')
        for curr in levels[E[i]%(maxDepth)]:
            if curr >= F[i]:
                minValue = min(minValue, curr)
        ans.append(minValue if minValue != float('inf') else -1)
    return ans


print(solve(5, [1, 4, 3, 1], [5, 2, 4, 4], [7, 38, 27, 37, 1], [1, 1, 2], [32, 18, 26]))