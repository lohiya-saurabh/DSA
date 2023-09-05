
class Queue:
    def __init__(self, size):
        self.max_size = size
        self.front = -1
        self.rear = -1
        self.queue = [0 for _ in range(size)]

    def enqueue(self, val):
        if (self.rear + 1) % self.max_size == self.front:
            self.rear = (self.rear + 1) % self.max_size
            self.queue[self.rear] = val
            self.front = (self.front + 1) % self.max_size
        elif self.front == -1:  # First element
            self.front = self.rear = 0
            self.queue[self.rear] = val
        else:
            self.rear = (self.rear + 1) % self.max_size
            self.queue[self.rear] = val

    def getQueueFront(self):
        if self.front == -1:
            # Queue is empty
            return
        return self.queue[self.front]

    def getQueueLast(self):
        if self.front == -1:
            # Queue is empty
            return
        return self.queue[self.rear]

    def dequeueFromRear(self):
        if self.front == -1:
            # Queue is empty
            return
        elif self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.rear = (self.rear - 1) % self.max_size

    def dequeueFromFront(self):
        if self.front == -1:
            # Queue is empty
            return
        elif self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.max_size


def slidingMaximum(A, B):
    queue = Queue(B)
    res = []
    for i, val in enumerate(A):
        # Remove all the elements from rear end of queue
        # that are smaller than val
        while queue.front != -1 and A[queue.getQueueLast()] > val:
            queue.dequeueFromRear()
        queue.enqueue(i)
        if i >= B - 1:
            if queue.getQueueFront() == i - B:
                queue.dequeueFromFront()
            res.append(A[queue.getQueueFront()])
    return sum(res)


print(slidingMaximum([2, 5, -1, 7, -3, -1, -2], 4))

# Generate Testcases for sliding window maximum
# for _ in range(2):
# n = random.randint(1, 100)
# k = random.randint(1, n)
# arr = [random.randint(1, 100) for _ in range(n)]
# print(arr, k)
# print(slidingMaximum(arr, k))
