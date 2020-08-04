"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""86. Partition List [Clean Code]
"""

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        h1 = p1 = ListNode(-1)
        h2 = p2 = ListNode(-1)
        curr = head
        while curr:
            if curr.val < x:
                p1.next = curr
                p1 = p1.next
            else:
                p2.next = curr
                p2 = p2.next
            curr = curr.next
        p2.next = None
        p1.next = h2.next
        return h1.next