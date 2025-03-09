# https://www.geeksforgeeks.org/problems/given-a-linked-list-of-0s-1s-and-2s-sort-it/1

class Solution:
    #Function to sort a linked list of 0s, 1s and 2s.
    def segregate(self, head):
        if not head or not head.next:
            return head
    
        zero_head = Node(0)
        one_head = Node(0)
        two_head = Node(0)
    
        zero = zero_head
        one = one_head
        two = two_head
    
        current = head
    
        while current:
            if current.data == 0:
                zero.next = current
                zero = zero.next
            elif current.data == 1:
                one.next = current
                one = one.next
            else:
                two.next = current
                two = two.next
            current = current.next
        
        two.next = None
    
        if one_head.next:
            zero.next = one_head.next
            one.next = two_head.next
        else:
            zero.next = two_head.next
        
    
        if zero_head.next:
            return zero_head.next
        elif one_head.next:
            return one_head.next
        else:
            return two_head.next