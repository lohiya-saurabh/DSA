def solve(A, B, C, D):
    graph = {}
    total = 0
    for edge in C:
        if edge[0] in graph:
            graph[edge[0]].append(edge[1])
        else:
            graph[edge[0]] = [edge[1]]
        if edge[1] in graph:
            graph[edge[1]].append(edge[0])
        else:
            graph[edge[1]] = [edge[0]]
    visited = set()
    for i in range(1, A + 1):
        if i in visited:
            continue
        queue = [i]
        grpStrength = 0
        currQueue = set()
        while queue:
            node = queue.pop()
            visited.add(node)
            grpStrength += B[node - 1]
            if node not in graph:
                continue
            for child in graph[node]:
                if child in visited or child in currQueue:
                    continue
                currQueue.add(child)
                queue.append(child)
        if grpStrength >= D:
            total += 1
    return total


print(solve(10, [7,9,3,2,9,1,6,4,10,8], [[1,5],[2,6],[3,7],[3,9],[3,10],[4,5],[4,7],[4,10],[5,7],[7,9]], 26))