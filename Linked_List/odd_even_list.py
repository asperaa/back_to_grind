"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""328. Odd Even Linked List
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
    
    def oddEvenList(self, head):
        if not head:
            return
        curr_odd = head
        head_even = curr_even = head.next
        while curr_even and curr_even.next:
            next_even = curr_even.next.next
            next_odd = curr_odd.next.next
            curr_odd.next = next_odd
            curr_even.next = next_even
            curr_even = next_even
            curr_odd = next_odd
        curr_odd.next = head_even
        return head
