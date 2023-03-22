class LinkedList:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next

    def deleteDuplicates(self, head):
        dummy = pre = LinkedList(0)
        dummy.next = head
        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
                pre.next = head
            else:
                pre = pre.next
                head = head.next
        return dummy.next


node7 = LinkedList(5)
node6 = LinkedList(4, node7)
node5 = LinkedList(4, node6)
node4 = LinkedList(3, node5)
node3 = LinkedList(3, node4)
node2 = LinkedList(2, node3)
node = LinkedList(1, node2)

node.deleteDuplicates(node)
