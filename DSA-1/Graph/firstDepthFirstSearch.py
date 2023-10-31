
def solve(A, B, C):
    graph = {}
    for i in range(1, len(A)):
        if A[i] in graph:
            graph[A[i]].append(i+ 1)
        else:
            graph[A[i]] = [i+1]
    queue = [C]
    visited = set()
    i = 0
    while i != len(queue):
        node = queue[i]
        visited.add(node)
        i += 1
        for neighbour in graph.get(node, []):
            if neighbour in visited:
                continue
            if neighbour == B:
                return 1
            queue.append(neighbour)
    return 0

print(solve([1,1,1,3,3,2,2,7,6], 9, 1))