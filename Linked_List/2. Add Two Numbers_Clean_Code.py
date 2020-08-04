"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""2. Add Two Numbers [Clean Code]
"""

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = curr = ListNode(-1)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            curr.next = ListNode(carry%10)
            curr = curr.next
            carry = carry // 10
        return dummy.next