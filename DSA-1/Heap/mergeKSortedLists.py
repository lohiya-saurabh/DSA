# Merge K sorted linked lists
# Given a list containing head pointers of N sorted linked lists.
# Merge these given sorted linked lists and return them as one sorted list.
def mergeKSortedLinkedLists(arr):
    heap = createHeap(arr)
    head = heap[0]
    heap = removeMinFromHeap(heap)
    tail = head
    while len(heap):
        tail.next = heap[0]
        tail = tail.next
        heap = removeMinFromHeap(heap)
    return head

def createHeap(arr):
    heap = []
    for i, ele in enumerate(arr):
        heap.append(ele)
        if i > 0:
            parentIndex = (i - 1)//2
            pi = parentIndex
            ci = i
            while heap[pi].data > ele.data:
                heap = swap(heap, ci, pi)
                ci = pi
                if ci > 0:
                    pi = (ci - 1)//2
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
        if rightChildIndex < len(heap) and heap[leftChildIndex].data > heap[rightChildIndex].data and heap[rightChildIndex].data < heap[smallestIndex].data:
            heap = swap(heap, parentIndex, rightChildIndex)
            parentIndex = rightChildIndex
        if leftChildIndex < len(heap) and heap[leftChildIndex].data < heap[smallestIndex].data:
            heap = swap(heap, parentIndex, leftChildIndex)
            parentIndex = leftChildIndex
        if smallestIndex == parentIndex:
            break
    return heap

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
    return arr


    
    