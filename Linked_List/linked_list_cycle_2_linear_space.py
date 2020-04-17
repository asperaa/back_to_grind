"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""142. Linked List Cycle II [Linear Space]
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
    
    def detectCycle(self, head):
        hash_set = set()
        curr_node = head
        while curr_node:
            if curr_node in hash_set:
                return curr_node
            hash_set.add(curr_node)
            curr_node = curr_node.next
        return None
            