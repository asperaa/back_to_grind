"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""1019. Next Greater Node In Linked List
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
            length += 1
            head = head.next
        return length
    
    def reverse(self, head):
        prev_node = next_node = None
        curr_node = head
        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        return prev_node
    
    def nextLargerNodes(self, head):
        length = self.get_length(head)
        stack = []
        curr_node = rev_head = self.reverse(head)
        next_larger_nodes = [None] * length 
        next_larger_nodes[length-1] = 0
        for i in range(length - 2, -1, -1):
            if curr_node.val > curr_node.next.val:
                stack.append(curr_node.val)
            else:
                while stack and curr_node.next.val >= stack[-1]:
                    stack.pop()
            next_larger_nodes[i] = stack[-1] if stack else 0
            curr_node = curr_node.next
        return next_larger_nodes        
