"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""21. Merge Two Sorted Lists
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
    
    def mergeTwoLists(self, head_1, head_2):
        if not head_1:
            return head_2
        if not head_2:
            return head_1
        result_head = result_mover = None
        while head_1 and head_2:
            if not result_head:
                if head_1.val <= head_2.val:
                    result_head = result_mover = head_1
                    head_1 = head_1.next
                else:
                    result_head = result_mover = head_2
                    head_2 = head_2.next
                continue
            if head_1.val <= head_2.val:
                result_mover.next = head_1
                head_1 = head_1.next
            else:
                result_mover.next = head_2
                head_2 = head_2.next
            result_mover = result_mover.next
        if head_1:
            result_mover.next = head_1
        if head_2:
            result_mover.next = head_2
        return result_head