"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""143. Reorder List
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
    
    def reverse(self, head):
        prev_node = next_node = None
        curr_node = head
        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        head = prev_node
        return head
    
    def break_ll_from_middle(self, head):
        slow_ptr = fast_ptr = head
        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        l1 = head
        l2 = slow_ptr.next
        slow_ptr.next = None
        return (l1, l2)

    def reorderList(self, head):
        if not head:
            return None
        l1, l2 = self.break_ll_from_middle(head)
        l2 = self.reverse(l2)
        while l2:
            next_l1 = l1.next
            next_l2 = l2.next
            l1.next = l2
            l2.next = next_l1
            l1 = next_l1
            l2 = next_l2
        return l1