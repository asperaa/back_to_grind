"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""82. Remove Duplicates from Sorted List II
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
        if not head:
            return None
        dummy = curr = ListNode(-1)
        dummy.next = head
        while curr and curr.next:
            dup_detected = False
            while curr.next.next and curr.next.val == curr.next.next.val:
                curr.next = curr.next.next
                dup_detected = True
            if dup_detected:
                curr.next = curr.next.next
                continue
            curr = curr.next
        return dummy.next
