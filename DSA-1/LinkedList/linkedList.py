class LinkedList:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next

    def swapPairs(self, head):
        if not head or not head.next:
            return head

        # Swapping the first two nodes
        first_node = head
        second_node = head.next
        first_node.next = self.swapPairs(second_node.next)
        second_node.next = first_node

        return second_node

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

    def addTwoNumber(self, A, B):
        carry = 0
        head = LinkedList(0)
        prev = head
        while A or B or carry:
            num1 = A.val if A else 0
            num2 = B.val if B else 0
            temp = num1 + num2 + carry
            rem = temp % 10
            carry = temp//10
            new_node = LinkedList(rem)
            prev.next = new_node
            prev = new_node
            A = A.next if A else None
            B = B.next if B else None
        return head.next

    def reverseKNodes(self, head, k):
        count = 0
        head = current = head
        prev = None
        while current and count < k:
            tmp = current.next
            current.next = prev
            prev = current
            current = tmp
            count += 1
        if current:
            head.next = self.reverseList(current, k)
        return prev

    def swapPairs(self, A):
        head = current = A
        prev = None
        res = head.next if head and head.next else head
        while current and current.next:
            tmp = current.next.next
            if prev:
                prev.next = current.next
            current.next.next = current
            current.next = tmp
            prev = current
            current = tmp
        return res

    def partitionList(self, head, target):

        return head

    def reverseLL(self, head):
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    def checkPalindrome(self, A):
        slow = A
        fast = A
        stack = []
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if fast:
            slow = slow.next
        while slow:
            stack.append(slow.val)
            slow = slow.next
        head = A

        while len(stack) > 0:
            if head.val != stack.pop():
                return 0
            head = head.next
        return 1

    def partitionList(self, head, target):
        tmp = head
        prev = None
        first_node_greater_than_target = None
        tail_of_first_node_greater_than_target = None
        while tmp and tmp.val < target:
            prev = tmp
            tmp = tmp.next
        first_node_greater_than_target = tmp
        while tmp and tmp.val >= target:
            tail_of_first_node_greater_than_target = tmp
            tmp = tmp.next
        if not prev:
            if tail_of_first_node_greater_than_target and tail_of_first_node_greater_than_target.next:
                head = tail_of_first_node_greater_than_target.next
            else:
                head = first_node_greater_than_target

        while tail_of_first_node_greater_than_target and tail_of_first_node_greater_than_target.next:
            if tail_of_first_node_greater_than_target.next.val < target:
                if prev:
                    prev.next = tail_of_first_node_greater_than_target.next
                tmp = tail_of_first_node_greater_than_target.next.next
                tail_of_first_node_greater_than_target.next.next = first_node_greater_than_target
                prev = tail_of_first_node_greater_than_target.next
                while tmp and tmp.val >= target:
                    tail_of_first_node_greater_than_target.next = tmp
                    tail_of_first_node_greater_than_target = tmp
                    tmp = tmp.next
                tail_of_first_node_greater_than_target.next = tmp
            else:
                tail_of_first_node_greater_than_target = tail_of_first_node_greater_than_target.next
        return head

    def removeDuplicates(self, head):
        prev = first = head
        while first and first.next:
            if first.val == first.next.val:
                node_val_to_deleted = first.val
                while first and first.val == node_val_to_deleted:
                    tmp = first.next
                    del first
                    first = tmp
                if head.val == node_val_to_deleted:
                    head = first
                else:
                    prev.next = first
            else:
                prev = first
                first = first.next
        return head

    def reverseWholeKNodes(self, head, k):
        total_nodes = 0
        tmp = head
        while tmp:
            tmp = tmp.next
            total_nodes += 1
        return self.reverseWholeKNodesHelper(head, total_nodes, k)

    def reverseWholeKNodesHelper(self, head, nodes_unchanged, k):
        count = 0
        head = current = head
        prev = None
        if nodes_unchanged < k:
            return head
        while current and count < k:
            tmp = current.next
            current.next = prev
            prev = current
            current = tmp
            count += 1
        if current:
            head.next = self.reverseWholeKNodesHelper(
                current, nodes_unchanged-k, k)
        return prev

    def copyRandomList(self, head):
        visitedHash = {}
        return self.__copyRandomListHelper(head, visitedHash)

    def __copyRandomListHelper(self, head, visitedHash):
        if head == None:
            return None

        if head in self.visitedHash:
            return self.visitedHash[head]

        node = LinkedList(head.val)
        visitedHash[head] = node
        node.next = self.__copyRandomListHelper(head.next)
        node.random = self.__copyRandomListHelper(head.random)

        return node


node7 = LinkedList(1)
node6 = LinkedList(2, node7)
node5 = LinkedList(3, node6)
node4 = LinkedList(4, node5)
node3 = LinkedList(3, node4)
node2 = LinkedList(2, node3)
node = LinkedList(1, node2)

ans = node.checkPalindrome(node)
print(ans)

# WAP to sort a list in python
