"""We are the captains of our ships. and we stay 'till the end. We see our stories through.
"""

"""86. Partition List
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

    def partition(self, head, x):
        dummy_head = curr_node = ListNode(0)
        dummy_head.next = head
        second_part_dummy_head = dummy_mover = ListNode(0)
        first_part_head = None
        first_part_prev = None
        while curr_node:
            while curr_node.next and curr_node.next.val >= x:
                dummy_mover.next = curr_node.next
                dummy_mover = dummy_mover.next 
                curr_node.next = curr_node.next.next
            if not first_part_head:
                first_part_head = curr_node.next
            first_part_prev = curr_node
            curr_node = curr_node.next
        dummy_mover.next = None
        if not first_part_head:
            return second_part_dummy_head.next
        first_part_prev.next = second_part_dummy_head.next
        return first_part_head

if __name__ == "__main__":
    ll = LinkedList()
    ll.push(90)
    ll.push(4)
    ll.push(3)
    ll.push(2)
    ll.push(5)
    ll.push(2)
    ll.print_list(ll.head)
    new_head = ll.partition(ll.head, 3)
    ll.print_list(new_head)