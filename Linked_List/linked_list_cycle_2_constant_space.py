"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""142. Linked List Cycle II
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
    
    def get_loop_length(self, head):
        slow_ptr = fast_ptr = head
        loop_length = 0
        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
            if slow_ptr == fast_ptr:
                slow_ptr = slow_ptr.next
                loop_length += 1
                while slow_ptr != fast_ptr:
                    slow_ptr = slow_ptr.next
                    loop_length += 1
                break
        return loop_length
    
    def detectCycle(self, head):
        slow_ptr = fast_ptr = head
        loop_length = self.get_loop_length(head)
        if loop_length == 0:
            return None
        while loop_length:
            fast_ptr = fast_ptr.next
            loop_length -= 1
        while slow_ptr != fast_ptr:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next
        return slow_ptr
