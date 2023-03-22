n = int(input())
edges = {}
for _ in range(n):
    edges[int(input())] = []

totalEdges = int(input())

for _ in range(totalEdges):
    A, B = list(map(int, input().split()))
    edges[A].append(B)
    # edges[B].append(A)

A = int(input())
B = int(input())


def BFS(root, dest, edges):
    if not root:
        return []
    queue = [root]
    visited = {}
    result = []
    while queue:
        node = queue.pop(0)
        if not node in visited:
            visited[node] = True
            result.append(node)
            for child in edges[node]:
                queue.append(child)
    print(result)
    return dest in result


print(BFS(A, B, edges))
print(str(2) + ',' + str(3))
