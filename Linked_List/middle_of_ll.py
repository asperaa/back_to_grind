class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
    
    def push(self, val):
        node = Node(val)
        if not self.head:
            self.head = node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = node

    def print_list(self):
        temp = self.head
        while temp.next:
            print(temp.val, end=" ")
            temp = temp.next

    def middleNode(self, head):
        slow_ptr = head
        fast_ptr = head
        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        return slow_ptr
    

if __name__ == "__main__":
    ll = LinkedList()
    ll.push(1)
    ll.push(2)
    print(ll.middleNode(ll.head).val)