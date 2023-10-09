class LinkedList:
    def __init__(self, val):
        self.val = val
        self.next = None

def solve(A):
    head = LinkedList(1)
    tmp = head
    for ele in range(2, A + 1):
        new_node = LinkedList(ele)
        tmp.next = new_node
        tmp = tmp.next
    tmp.next = head
    tmp = head
    while tmp.next and tmp != tmp.next:
        next_ = tmp.next.next
        tmp.next = next_
        kill_ = tmp.next
        tmp = next_
        del kill_
    return tmp.val

print(solve(100))

