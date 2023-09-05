def cycleDetectionAlgorithm(A, B):
    graph = {}
    visited = set()
    for edge in B:
        if edge[0] in graph:
            graph[edge[0]].append(edge[1])
        else:
            graph[edge[0]] = [edge[1]]

    queue = []
    for node in range(1, A + 1):
        queue.append(node)
        node = queue.pop(0)
        if not node in visited and node in graph:
            visited.add(node)
            for children in graph[node]:
                if children in visited:
                    return 1
                queue.insert(0, children)
    return 0


A = 5
B = [[1, 2], [4, 1], [2, 4], [3, 4], [5, 2], [1, 3]]
