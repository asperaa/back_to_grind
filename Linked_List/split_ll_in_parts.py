"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""725. Split Linked List in Parts
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
    
    def split(self, head, split_size):
        second_part = head
        while split_size:
            prev = second_part
            second_part = second_part.next
            split_size -= 1
        prev.next = None
        first_part = head
        return (first_part, second_part)
    
    def handle_k_greater_than_length(self, head, k, length):
        parts = []
        non_null_parts = length
        l2 = head
        while non_null_parts:
            l1, l2 = self.split(l2, 1)
            parts.append(l1)
            non_null_parts -= 1
        null_parts = k - length
        while null_parts:
            parts.append(None)
            null_parts -= 1
        return parts

    def handle_k_smaller_than_length(self, head, k, length):
        num_of_big_parts = length % k
        num_of_small_parts = k - num_of_big_parts
        big_part_elements = length // k + 1
        parts = []
        l2 = head
        while num_of_big_parts:
            l1, l2 = self.split(l2, big_part_elements)
            parts.append(l1)
            num_of_big_parts -= 1
        while num_of_small_parts:
            l1, l2 = self.split(l2, big_part_elements - 1)
            parts.append(l1)
            num_of_small_parts -= 1
        return parts
    
    def splitListToParts(self, head, k):
        length = self.get_length(head)
        if k >= length:
            return self.handle_k_greater_than_length(head, k, length)
        else:
            return self.handle_k_smaller_than_length(head, k, length)