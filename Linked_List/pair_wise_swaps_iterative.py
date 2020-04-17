"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""24. Swap Nodes in Pairs [Iterative]
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
    
    def swapPairs(self, head):
        dummy = prev = ListNode(-1)
        dummy.next = curr = head
        while curr and curr.next:
            first_node = curr
            second_node = curr.next

            prev.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            prev = first_node
            curr = first_node.next
        return dummy.next
