def solve(A):
    totalCost = 0
    heap = createHeap(A)
    i, n = 0, len(heap)
    while len(heap):
        A = heap[0]
        heap = removeMinFromHeap(heap)
        B = heap[0] if len(heap) else 0
        heap = removeMinFromHeap(heap) if heap else []
        new_rope = A + B
        totalCost += new_rope
        heap = insertIntoHeap(heap, new_rope) if heap else []
    return totalCost

def insertIntoHeap(heap, ele):
    heap.append(ele)
    childIndex = len(heap) - 1
    parentIndex = (childIndex - 1)//2
    while heap[parentIndex] > ele:
        heap = swap(heap, childIndex, parentIndex)
        childIndex = parentIndex
        if childIndex > 0:
            parentIndex = (childIndex - 1)//2
        else:
            break
    return heap

def removeMinFromHeap(heap):
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

def createHeap(arr):
    heap = []
    for i, ele in enumerate(arr):
        heap.append(ele)
        if i > 0:
            parentIndex = (i - 1)//2
            pi = parentIndex
            ci = i
            while heap[pi] > ele:
                heap = swap(heap, ci, pi)
                ci = pi
                if ci > 0:
                    pi = (ci - 1)//2
                else:
                    break
    return heap

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
    return arr

print(solve([1,2,3]))