def solve(A):
    gen = ["1", "2", "3"]
    res = []
    curr_queue = []
    flag = True
    while len(res) < A:
        next_queue_len = len(res)
        while curr_queue or flag:
            flag = False
            curr_elem = curr_queue.pop(0) if curr_queue else ""
            for elem in gen:
                if len(res) < A:
                    res.append(curr_elem + elem)
                else:
                    break
        curr_queue = res[next_queue_len:]
    return [int(x) for x in res]
    # Generate a test case


print(solve(10))
