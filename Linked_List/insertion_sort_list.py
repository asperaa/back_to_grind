"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""147. Insertion Sort List
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
    
    def insertion_sort(self, head):
        if not head:
            return None
        dummy = dummy_mover = ListNode(0)
        dummy.next = curr = head
        while curr.next:
            insertee = curr.next
            curr.next = curr.next.next
            dummy_mover = dummy
            while dummy_mover != curr:
                if insertee.val <= dummy_mover.next.val:
                    insertee.next = dummy_mover.next
                    dummy_mover.next = insertee
                    break
                dummy_mover = dummy_mover.next
            if dummy_mover == curr:
                insertee.next = dummy_mover.next
                dummy_mover.next = insertee
                curr = curr.next
        return dummy.next


if __name__ == "__main__":
    ll = LinkedList()
    ll.push(4)
    ll.push(5)
    ll.push(2)
    ll.push(90)
    ll.push(0)
    ll.push(5)
    ll.push(-1)
    ll.push(-2)
    head = ll.insertion_sort(ll.head)
    ll.print_list(head)
        
