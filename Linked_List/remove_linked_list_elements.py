"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""203. Remove Linked List Elements
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
    
    def removeElements(self, head, k):
        dummy = curr = ListNode(-1)
        dummy.next = head
        while curr.next:
            while curr.next.val == k:
                curr.next = curr.next.next
                if not curr.next:
                    return dummy.next
            curr = curr.next
        return dummy.next
