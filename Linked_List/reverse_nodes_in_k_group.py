"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""25. Reverse Nodes in k-Group
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
    

    def reverse_K_helper(self, head, k):
        prev_node = next_node = None
        curr_node = temp = head
        for i in range(k):
            if not temp:
                return (head, None)
            temp = temp.next
        while k:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
            k -= 1
        return (prev_node, next_node)

    def reverseKGroup(self, head, k):
        dummy_head = dummy_mover = ListNode(0)
        dummy_head.next = next_head = head
        while next_head:
            new_tail = next_head
            rev_head, next_head = self.reverse_K_helper(next_head, k)
            dummy_mover.next = rev_head
            dummy_mover = new_tail
        return dummy_head.next

if __name__ == "__main__":
    ll = LinkedList()
    ll.push(1)
    ll.push(2)
    # ll.push(3)
    # ll.push(4)
    # ll.push(5)
    # ll.push(6)
    head = ll.reverseKGroup(ll.head, 2)
    ll.print_list(head)

