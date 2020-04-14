"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""83. Remove Duplicates from Sorted List
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
    
    def deleteDuplicates(self, head):
        curr_node = head
        while curr_node and curr_node.next:
            while curr_node.next and curr_node.val == curr_node.next.val:
                curr_node.next = curr_node.next.next
            curr_node = curr_node.next
        return curr_node