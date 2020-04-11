class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def push(self, val):
        node = ListNode(val)
        if not self.head:
            self.head = node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = node
    
    def addTwoNumbers(self, l1, l2):
        result_ll = None
        carry = 0
        while l1 and l2:
            single_sum = (l1.val + l2.val + carry) % 10
            carry = (l1.val + l2.val + carry) // 10
            new_node = ListNode(single_sum)
            if not result_ll:
                result_ll = new_node
                result_head = result_ll
                l1 = l1.next
                l2 = l2.next
                continue
            result_ll.next = new_node
            result_ll = result_ll.next
            l1 = l1.next
            l2 = l2.next
        
        result_ll, carry = self.handle_long_ll(result_ll, l1, carry)
        result_ll, carry = self.handle_long_ll(result_ll, l2, carry)

        if carry:
            result_ll.next = ListNode(1)
        return result_head

    def handle_long_ll(self, result_ll, ll, carry):
        while ll:
            single_sum = (ll.val + carry) % 10
            carry = (ll.val + carry) // 10
            new_node = ListNode(single_sum)
            result_ll.next = new_node
            result_ll = result_ll.next
            ll = ll.next
        return (result_ll, carry)

