def solve(A, B):
    inDegree = [0] * (A + 1)
    neighbours = [[] for _ in range(A + 1)]
    for edge in B:
        inDegree[edge[1]] += 1
        neighbours[edge[0]].append(edge[1])
    queue = []
    for i in range(1, A + 1):
        if inDegree[i] == 0:
            minHeapify(queue, i)
    final = []
    while queue:
        node = queue[0]
        final.append(node)
        heapifyDown(queue)
        for child in neighbours[node]:
            inDegree[child] -= 1
            if inDegree[child] == 0:
                minHeapify(queue, child)
    return final

def minHeapify(heap, num):
    heap.append(num)
    childIndex = len(heap) - 1
    parentIndex = (childIndex - 1)//2
    while heap[parentIndex] > num:
        heap = swap(heap, childIndex, parentIndex)
        childIndex = parentIndex
        if childIndex > 0:
            parentIndex = (childIndex - 1)//2
        else:
            break
    return heap

def heapifyDown(heap):
    heap = swap(heap, 0, len(heap) - 1)
    heap.pop()
    parentIndex = 0
    while True:
        leftChildIndex = 2 * parentIndex + 1
        rightChildIndex = 2 * parentIndex + 2
        smallestIndex = parentIndex
        if rightChildIndex < len(heap) and heap[leftChildIndex] > heap[rightChildIndex] and heap[rightChildIndex] < heap[smallestIndex]:
            heap = swap(heap, parentIndex, rightChildIndex)
            parentIndex = rightChildIndex
        if leftChildIndex < len(heap) and heap[leftChildIndex] < heap[smallestIndex]:
            heap = swap(heap, parentIndex, leftChildIndex)
            parentIndex = leftChildIndex
        if smallestIndex == parentIndex:
            break
    return heap        
                
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
    return arr    

print(solve(8, [[1,4],[1,2],[4,2],[4,3],[3,2],[5,2],[3,5],[8,2],[8,6]]))