"""We are the captains of our ships, and we stay 'till the end. we see our stories through.
"""

"""92. Reverse Linked List II
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
    
    def reverse_helper(self, m_head, rev_length):
        prev_node = next_node = None
        curr_node = m_head
        while rev_length:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
            rev_length -= 1
        rev_m_head = prev_node
        next_of_nth_node = next_node
        return (rev_m_head, next_of_nth_node)
    
    def reverseBetween(self, head, m , n):
        dummy_head = dummy_curr = ListNode(0)
        dummy_head.next = head
        rev_length = n - m + 1
        while m:
            prev_dummy = dummy_curr
            dummy_curr = dummy_curr.next
            m -= 1
        rev_m_head, next_of_nth_node = self.reverse_helper(dummy_curr, rev_length)
        prev_dummy.next = rev_m_head
        dummy_curr.next = next_of_nth_node
        return dummy_head.next