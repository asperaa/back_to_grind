"""We are the captains of our ships, and we stay till the end. We see our stories through."""
class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
    
    def print_list(self, head=None):
        temp = head
        while temp:
            print(temp.val, end=" ")
            temp = temp.next
        print()
    
    def push(self, val):
        node = ListNode(val)
        if not self.head:
            self.head = node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = node
    
    def reverseList(self, head):
        prev_node = next_node = None
        curr_node = head
        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        new_head = prev_node
        return new_head

if __name__ == "__main__":
    ll = LinkedList()
    ll.push(1)
    ll.push(2)
    ll.push(3)
    ll.print_list(ll.head)
    new_head = ll.reverseList(ll.head)
    ll.print_list(new_head)