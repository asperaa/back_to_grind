"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""19. Remove Nth Node From End of List
"""

class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
    
    def push(self, val):
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        mover = self.head
        while mover.next:
            mover = mover.next
        mover.next = new_node
    
    def print_list(self, head):
        mover = head
        while mover:
            print(mover.val, end=" ")
            mover = mover.next
        print()
    
    def removeNthFromEnd(self, head, n):
        fast_ptr = slow_ptr = head
        while n:
            n -= 1
            fast_ptr = fast_ptr.next
        if not fast_ptr:
            return slow_ptr.next
        while fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next
        slow_ptr.next = slow_ptr.next.next
        return head