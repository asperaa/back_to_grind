"""We are the captains of our ships, and we stay 'till the end. We see our stories through."""
"""Method-1- LL is modified."""

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
        mover =  self.head
        while mover.next:
            mover = mover.next
        mover.next = new_node
    
    def reverse(self, head):
        prev_node = next_node = None
        curr_node = head
        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        new_head = prev_node
        return new_head
    
    def add_two_numbers(self, head_1, head_2):
        rev_mover_1 = self.reverse(head_1)
        rev_mover_2 = self.reverse(head_2)
        result_head = result_mover = None
        carry = 0
        while rev_mover_1 and rev_mover_2:
            summ = (rev_mover_1.val + rev_mover_2.val + carry) % 10
            sum_node = ListNode(summ)
            carry = (rev_mover_1.val + rev_mover_2.val + carry) // 10
            if not result_head:
                result_head = result_mover = sum_node
                rev_mover_1 = rev_mover_1.next
                rev_mover_2 = rev_mover_2.next
                continue
            result_mover.next = sum_node
            result_mover = result_mover.next
            rev_mover_1 = rev_mover_1.next
            rev_mover_2 = rev_mover_2.next
        
        result_mover, carry = self.handle_longer_list(result_mover, rev_mover_1, carry)
        result_mover, carry = self.handle_longer_list(result_mover, rev_mover_2, carry)

        if carry:
            result_mover.next = ListNode(1)
        result_head = self.reverse(result_head)
        return result_head
    
    def handle_longer_list(self, result_mover, rev_mover, carry):
        while rev_mover:
            sum_node = ListNode((rev_mover.val + carry) % 10)
            carry = (rev_mover.val + carry) // 10
            result_mover.next = sum_node
            result_mover = result_mover.next
            rev_mover = rev_mover.next
        return (result_mover, carry)
    
    def print_list(self, head):
        mover = head
        while mover:
            print(mover.val, end=" ")
            mover = mover.next
        print()

if __name__ == "__main__":
    l1 = LinkedList()
    l1.push(1)
    l1.push(2)
    l1.push(3)
    l2 = LinkedList()
    l2.push(4)
    l2.push(5)
    result_head = l1.add_two_numbers(l1.head, l2.head)
    l1.print_list(result_head)