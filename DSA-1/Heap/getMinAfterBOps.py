def solve(A, B):
    heap = createHeap(A)
    heap = [[val, val] for val in heap]
    i = 0
    while i < B:
        heap[0][0] += heap[0][1]
        heap = minHeapDown(heap)
        i += 1
    return max([val[0] for val in heap])

def minHeapDown(heap):
    parentIndex = 0
    while True:
        leftChildIndex = 2 * parentIndex + 1
        rightChildIndex = 2 * parentIndex + 2
        smallestIndex = parentIndex
        if rightChildIndex < len(heap) and heap[leftChildIndex][0] + heap[leftChildIndex][1] > heap[rightChildIndex][0] + heap[rightChildIndex][1] and heap[rightChildIndex][0] + heap[rightChildIndex][1] < heap[smallestIndex][0] + heap[smallestIndex][1]:
            heap = swap(heap, parentIndex, rightChildIndex)
            parentIndex = rightChildIndex
        if leftChildIndex < len(heap) and heap[leftChildIndex][0] + heap[leftChildIndex][1]< heap[smallestIndex][0] + heap[smallestIndex][1]:
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

print(solve([8, 6, 4, 2], 8))


# def solve(A, B):
#     heap = createHeap(A)
#     heap = [[val, val] for val in A]
#     i = 0
#     while i < B:
#         heap[0][0] += heap[0][1]
#         heap = minHeapDown(heap)
#         i += 1
#     return max([val[0] for val in heap] )

# def minHeapDown(heap):
#     parentIndex = 0
#     while True:
#         leftChildIndex = 2 * parentIndex + 1
#         rightChildIndex = 2 * parentIndex + 2
#         smallestIndex = parentIndex
#         if rightChildIndex < len(heap) and heap[leftChildIndex][0] > heap[rightChildIndex][0] and heap[rightChildIndex][0] < heap[smallestIndex][0]:
#             heap = swap(heap, parentIndex, rightChildIndex)
#             parentIndex = rightChildIndex
#         if leftChildIndex < len(heap) and heap[leftChildIndex][0] < heap[smallestIndex][0]:
#             heap = swap(heap, parentIndex, leftChildIndex)
#             parentIndex = leftChildIndex
#         if smallestIndex == parentIndex:
#             break
#     return heap

# def createHeap(arr):
#     heap = []
#     for i, ele in enumerate(arr):
#         heap.append(ele)
#         if i > 0:
#             parentIndex = (i - 1)//2
#             pi = parentIndex
#             ci = i
#             while heap[pi] > ele:
#                 heap = swap(heap, ci, pi)
#                 ci = pi
#                 if ci > 0:
#                     pi = (ci - 1)//2
#                 else:
#                     break
#     return heap

# def swap(arr, i, j):
#     arr[i], arr[j] = arr[j], arr[i]
#     return arr

# print(solve([1,2,3], 5))