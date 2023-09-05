def solve(A):
    queue = ["1", "2"]
    queueAppender = ["1", "2"]
    while A:
        currQueueSize = len(queue)
        nextQueue = []
        if len(queue) >= A:
            return int(queue[A - 1] + queue[A - 1][::-1])
        while queue:
            ele = queue.pop(0)
            for appender in queueAppender:
                nextQueue.append(ele + appender)
        queue = nextQueue
        A -= currQueueSize


print(solve(4))
