"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""61. Rotate List
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
    
    def get_length(self, head):
        length = 0
        while head:
            head = head.next
            length += 1
        return length

    def rotateRight(self, head, k):
        if not head:
            return None
        length = self.get_length(head)
        old_tail_end = head
        while old_tail_end.next:
            old_tail_end = old_tail_end.next
        old_tail_end.next = head
        k = k%length
        new_tail_distance = length - k - 1
        new_tail = head
        while new_tail_distance:
            new_tail = new_tail.next
            new_tail_distance -= 1
        new_head = new_tail.next
        new_tail.next = None
        return new_head

            
        

if __name__ == "__main__":
    ll = LinkedList()
    ll.push(1)
    ll.push(2)
    # ll.push(3)
    # ll.push(4)
    # ll.push(5)
    new = ll.rotateRight(ll.head, 1)
    ll.print_list(new)
