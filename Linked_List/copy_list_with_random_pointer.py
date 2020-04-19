"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""138. Copy List with Random Pointer
"""

class Node:
    
    def __init__(self, val):
        self.val = val
        self.next = None
        self.random = None
    
class LinkedList:

    def __init__(self):
        self.head = None
    
    def push(self, val):
        new_node = Node(val)
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
    
    def copyRandomList(self, head):
        if not head:
            return head
        curr = head
        while curr:
            next_node = curr.next
            new_node = Node(curr.val)
            curr.next = new_node
            new_node.next = next_node
            curr = next_node
        curr = head
        while curr:
            curr.next.random = getattr(curr.random, 'next', None)
            curr = curr.next.next
        l1 = l1_mover = Node(-1)
        l2 = l2_mover = Node(-1)
        l2.next = l1.next = head
        curr = head
        while curr:
            l1_mover.next = curr
            l1_mover = l1_mover.next
            curr = curr.next
            l2_mover.next = curr
            l2_mover = l2_mover.next
            curr = curr.next
        return l2.next        