"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""206. Reverse Linked List [Recursion]
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
    
    def reverse_helper(self, head):
        if not head.next:
            rev_head = head
            return (rev_head, head)
        rev_head, curr_node = self.reverse_helper(head.next)
        curr_node.next = head
        return (rev_head, head)

    def reverse(self, head):
        if not head:
            return head
        rev_head, rev_tail = self.reverse_helper(head)
        rev_tail.next = None
        return rev_head

if __name__ == "__main__":
    ll = LinkedList()
    ll.push(1)
    ll.push(2)
    ll.push(3)
    rev_head = ll.reverse(ll.head)
    ll.print_list(rev_head)