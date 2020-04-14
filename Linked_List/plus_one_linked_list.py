"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""369. Plus One Linked List
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

    def plus_one_helper(self, head):
        if not head:
            return (None, 1)
        result_head, carry = self.plus_one_helper(head.next)
        sum_node = ListNode((head.val + carry) % 10)
        carry = (head.val + carry) // 10
        sum_node.next = result_head
        return (sum_node, carry)
        

    def plusOne(self, head):
        result_head, carry = self.plus_one_helper(head)
        if carry:
            new_node = ListNode(1)
            new_node.next = result_head
            result_head = new_node
        return result_head

if __name__ == "__main__":
    ll = LinkedList()
    ll.push(9)
    result_head = ll.plusOne(ll.head)
    ll.print_list(result_head)
