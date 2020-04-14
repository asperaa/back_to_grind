"""We are the captains of our ships, and we stay 'till the end. We see out stories through.
"""

"""160. Intersection of Two Linked Lists
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
        mover = head
        while mover:
            length += 1
            mover = mover.next
        return length
    
    def get_new_mover(self, length_diff, head):
        while length_diff:
            head = head.next
            length_diff -= 1
        return head

    def getIntersectionNode(self, head_1, head_2):
        length_1 = self.get_length(head_1)
        length_2 = self.get_length(head_2)
        if length_1 > length_2:
            head_1 = self.get_new_mover(length_1 - length_2, head_1)
        else:
            head_2 = self.get_new_mover(length_2 - length_1, head_2)
        while head_1 and head_2:
            if head_1 == head_2:
                return head_1
            head_1 = head_1.next
            head_2 = head_2.next
        return None

if __name__ == "__main__":
    l1 = LinkedList()
    l1.push(1)
    l1.push(2)
    l1.push(3)
    l1.push(4)
    l1.push(5)
    l1.push(6)
    l2 = LinkedList()
    l2.push(7)
    l2.push(89)
    l2.push(65)
    l2.head.next.next.next = l1.head.next.next.next
    print(l1.getIntersectionNode(l1.head, l2.head).val)