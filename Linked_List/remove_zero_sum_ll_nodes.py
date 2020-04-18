"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""1171. Remove Zero Sum Consecutive Nodes from Linked List
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
    
    def removeZeroSumSublists(self, head):
        dummy = curr = ListNode(0)
        dummy.next = head
        curr_sum = 0
        seen = {}
        while curr:
            curr_sum += curr.val
            seen[curr_sum] = curr
            curr = curr.next
        curr_sum = 0
        curr = dummy
        while curr:
            curr_sum += curr.val
            curr.next = seen[curr_sum].next
            curr = curr.next
        return dummy.next