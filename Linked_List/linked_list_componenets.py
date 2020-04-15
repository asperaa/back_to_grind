"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""817. Linked List Components
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
    
    def numComponents(self, head, G):
        hash_set = set(G)
        num_components = 0
        curr_node = head
        while curr_node:
            if curr_node.val in hash_set and getattr(curr_node.next, 'val', None) not in hash_set:
                num_components += 1
            curr_node = curr_node.next
        return num_components