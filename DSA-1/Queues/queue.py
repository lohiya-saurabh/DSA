
class Queue:
    def __init__(self, size):
        self.size = size
        self.f = -1
        self.r = -1
        self.capacity = 0
        self.queue = []

    def enqueue(self, val):
        if self.size == self.capacity:
            self.f = (self.f + 1) % self.size
        self.r = (self.r + 1) % self.size
        self.queue[self.r] = val
        if self.capacity < self.size:
            self.capacity += 1

    def front(self):
        if self.capacity == 0:
            return
        return self.f

    def rear(self):
        if self.capacity == 0:
            return
        return self.queue[self.r]

    def dequeueFromRear(self):
        if self.capacity != 0:
            if self.r == 0:
                self.r = self.size - 1
            else:
                self.r = self.r - 1
            self.capacity -= 1
