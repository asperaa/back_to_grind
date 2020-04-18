"""We are the captains of our ship, and we stay 'till the end. We see our stories through.
"""

"""148. Sort List
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
    
    def merge(self, l1, l2):
        dummy = prev = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        prev.next = l1 if l1 else l2
        return dummy.next

    def mid_break(self, head):
        slow_ptr = fast_ptr = head
        while fast_ptr and fast_ptr.next:
            prev_slow_ptr = slow_ptr
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        first_part, second_part = head, prev_slow_ptr.next
        prev_slow_ptr.next = None
        return (first_part, second_part)

    def sortList(self, head):
        if not head:
            return None
        if head.next:
            first_part, second_part = self.mid_break(head)
            sorted_first_part = self.sortList(first_part)
            sorted_second_part = self.sortList(second_part)
            head = self.merge(sorted_first_part, sorted_second_part)
        return head

if __name__ == "__main__":
    ll = LinkedList()
    ll.push(4)
    ll.push(3)
    ll.push(6)
    ll.push(1)
    ll.push(-1)
    head = ll.sortList(ll.head)
    ll.print_list(head)