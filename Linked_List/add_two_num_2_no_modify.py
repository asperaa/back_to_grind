"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""
class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def print_list(self, head):
        mover = head
        while mover:
            print(mover.val, end=" ")
            mover = mover.next
        print()
    
    def push(self, val):
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        mover = self.head
        while mover.next:
            mover = mover.next
        mover.next = new_node
    
    def get_length(self, head):
        length = 0
        mover = head
        while mover:
            length += 1
            mover = mover.next
        return length
    
    def add_zeros(self, head, num_zeroes):
        while num_zeroes:
            new_node = ListNode(0)
            new_node.next = head
            head = new_node
            num_zeroes -= 1
        return head
    
    def add_two_num_helper(self, head_1, head_2):
        if not head_1 and not head_2:
            return (None, 0)
        result_head, carry = self.add_two_num_helper(head_1.next, head_2.next)
        sum_node = ListNode((head_1.val + head_2.val + carry) % 10)
        carry = (head_1.val + head_2.val + carry) // 10
        sum_node.next = result_head
        return sum_node, carry

    def add_two_num(self, head_1, head_2):
        length_1 = self.get_length(head_1)
        length_2 = self.get_length(head_2)
        if length_1 > length_2:
            head_2 = self.add_zeros(head_2, length_1 - length_2)
        else:
            head_1 = self.add_zeros(head_1, length_2 - length_1)
        result_head, carry = self.add_two_num_helper(head_1, head_2)
        if carry:
            new_node = ListNode(1)
            new_node.next = result_head
            result_head = new_node
        return result_head

if __name__ == "__main__":
    l1 = LinkedList()
    l1.push(1)
    l1.push(2)
    l1.push(3)
    l2 = LinkedList()
    l2.push(4)
    l2.push(5)
    result_head = l1.add_two_num(l1.head, l2.head)
    l1.print_list(result_head)
